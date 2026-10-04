---
tags: [excel-advanced, tier3]
area: Excel Advanced
topic: "VBA, Macros & Office Scripts Basics"
tier: Tier 3
roles: Analytics / Operations
status: complete
subtopics: 13
---
# VBA, Macros & Office Scripts Basics

⬅ [[188 Financial Modelling in Excel]] · [[_Index - Excel Advanced|Excel Advanced]]

> **Area:** Excel Advanced · **Priority:** 🟡 Tier 3 · **Target roles:** Analytics / Operations

## Sub-topics in this note
1. [[#1. Why VBA Still Matters, and When Not to Use It]]
2. [[#2. Setting Up: Developer Tab, the Recorder and File Types]]
3. [[#3. The Excel Object Model: Application, Workbook, Worksheet, Range]]
4. [[#4. Variables, Data Types and Option Explicit]]
5. [[#5. Control Flow: If, Select Case, For, For Each, Do While]]
6. [[#6. Fast, Reliable Range Code: Arrays, ScreenUpdating and Calculation]]
7. [[#7. Procedures, Functions and User-Defined Functions]]
8. [[#8. Error Handling and Defensive Code]]
9. [[#9. Automating Files: Import and Consolidate a Folder of CSVs]]
10. [[#10. Report Automation: Split by Plant and Export PDF]]
11. [[#11. Events and User Forms]]
12. [[#12. Security: Macros, Trust and Distribution]]
13. [[#13. ⭐ Advanced: Alternatives and the Modern Automation Stack]]

## 📰 News box
> [!news] Shared news hook for this topic (2022-2026): Microsoft blocks internet macros by default, and the web-first alternative is Office Scripts
> **Macros in files from the internet are blocked by default (Windows desktop Office).** Microsoft changed Office so that VBA macros in files that carry the "Mark of the Web" no longer offer an "Enable content" button: the user sees a Security Risk banner instead and must unblock the file first (right-click, Properties, tick **Unblock**, or run `Unblock-File` in PowerShell). The rollout ran from Current Channel Preview (version 2203, 12 April 2022) to Semi-Annual Enterprise Channel (version 2208, 10 January 2023); Publisher followed on 14 February 2023 and Project on 13 August 2024. It affects Windows only, not macOS, mobile or Office on the web. A macro file you download from email or a shared link may therefore refuse to run until it is unblocked or stored in a trusted location. ([Microsoft Learn: Macros from the internet are blocked by default](https://learn.microsoft.com/en-us/microsoft-365-apps/security/internet-macros-blocked); checked 4 October 2026)
>
> **Office Scripts.** Microsoft documents Office Scripts as TypeScript/JavaScript-based automation, web-first (Excel on the web, with limited desktop support), recordable with an Action Recorder, stored in OneDrive, and designed to be called from Power Automate flows; it needs a Microsoft 365 subscription. Microsoft's own comparison positions it as the cloud-integrated alternative to desktop-focused VBA. The same page notes that built-in script scheduling was temporarily disabled and that Power Automate flows are the workaround. ([Microsoft Learn: Office Scripts in Excel](https://learn.microsoft.com/en-us/office/dev/scripts/overview/excel); checked 4 October 2026)
>
> Sub-topics that say **"See news box"** reuse these items.

---
## 1. Why VBA Still Matters, and When Not to Use It
> 🟡 Tier 3 · _Key points:_ desktop automation, legacy workbooks, decision grid vs Power Query, Python, Office Scripts

### Definition
**VBA (Visual Basic for Applications)** is the macro language built into desktop Excel, Word and Access. A **macro** is a stored procedure (`Sub`) that automates actions. VBA is still found in plant, finance and logistics workbooks because it can drive anything the desktop application can do: loop over files, edit workbooks, send Outlook mail, refresh pivots, export PDFs, and build forms. Its weaknesses: it runs only in desktop Office (not Excel on the web), macro-enabled files are a security target, code is hard to version and test, and a macro that selects cells and cuts and pastes is slow and fragile.

Pick the tool by the job:

| Job | Best first choice | Why |
|---|---|---|
| Import, clean, append CSV/ERP exports | Power Query ([[075 Pivot Tables & Power Query]]) | Repeatable, no code, refreshable |
| Heavy transformation, statistics, forecasting | Python ([[186 Python Data Cleaning & EDA Playbook]], [[046 Python for Operations]]) | Libraries, testing, version control |
| Automate cloud-based workbooks, scheduled flows | Office Scripts + Power Automate | Web-first, no desktop needed |
| Desktop UI actions, forms, legacy files, per-row loops that must write formats | VBA | Full control of the Excel object model |
| One-off cleanup | Formulas and filters ([[070 Foundations & Navigation]]) | No automation needed |

### Example
A plant MIS team receives a daily ERP stock export (CSV). Cleaning it is a Power Query job (refresh in one click). Producing a **formatted, plant-wise PDF pack e-mailed to 12 plant heads** is a VBA job, because it needs to filter, format, export and mail. Mixing the two (Power Query for the data, one small VBA macro for the PDF export) is typical.

### In the news
See news box. The macro-blocking default pushes organisations toward trusted locations, signed macros, or alternatives such as Office Scripts and Power Automate.

### Interview angle
> [!question] How it is asked
> "Have you used VBA? When would you use a macro rather than Power Query or Python?"

> [!tip] Strong answer includes
> - A decision rule (data transformation: Power Query; heavy analytics: Python; desktop UI automation or legacy files: VBA)
> - One concrete automation you built or would build, with before/after time saved
> - Awareness of the security and maintainability costs (.xlsm risk, undocumented code)
> - Mention of Office Scripts or Power Automate for cloud workbooks

---
## 2. Setting Up: Developer Tab, the Recorder and File Types
> 🟡 Tier 3 · _Key points:_ Developer tab, Alt+F11, .xlsm vs .xlsx, recorder, relative references

### Definition
Enable the **Developer** tab (File, Options, Customize Ribbon). Open the **VBA editor** with `Alt+F11`. Code lives in **modules** (Insert, Module), in **sheet/workbook objects** (event code) and in **user forms**. A workbook containing macros must be saved as **.xlsm** (macro-enabled) or **.xlsb**; a plain `.xlsx` cannot store macros. The personal macro workbook (`PERSONAL.XLSB`) holds macros available in every file.

The **Macro Recorder** (Developer, Record Macro) writes VBA from your clicks. Use it to learn syntax and object names, then clean the result. Recorded code is verbose and relies on `Select` and `ActiveCell`; use **Use Relative References** when a recorded action should work from the current cell rather than fixed addresses.

### Example
Record a macro that formats a header row bold with a fill colour, then inspect it:
```vba
Sub FormatHeader()
    Range("A1:F1").Select
    Selection.Font.Bold = True
    Selection.Interior.Color = RGB(221, 235, 247)
End Sub
```
Cleaned version (no `Select`):
```vba
Sub FormatHeader()
    With Range("A1:F1")
        .Font.Bold = True
        .Interior.Color = RGB(221, 235, 247)
    End With
End Sub
```

### In the news
See news box. Because internet-sourced macro files are blocked by default, save your own tools in a **trusted location** or distribute them as add-ins (.xlam) rather than emailing .xlsm files.

### Interview angle
> [!question] How it is asked
> "You recorded a macro and it is slow and breaks on new data. What do you do?"

> [!tip] Strong answer includes
> - Remove `Select`/`Activate`; refer to ranges directly
> - Replace hard-coded addresses with last-row logic or Tables
> - Turn off screen updating while it runs
> - Test on a copy of the file

---
## 3. The Excel Object Model: Application, Workbook, Worksheet, Range
> 🟡 Tier 3 · _Key points:_ object hierarchy, properties vs methods, Cells vs Range, ThisWorkbook vs ActiveWorkbook

### Definition
VBA controls Excel through **objects** arranged in a hierarchy: `Application` contains `Workbooks`, each containing `Worksheets`, each containing `Range` objects. Objects have **properties** (values you read or set, like `.Value`, `.Font.Bold`) and **methods** (actions, like `.Copy`, `.ClearContents`, `.Sort`). Common references:

```vba
ThisWorkbook                           ' the workbook that holds the code
ActiveWorkbook                         ' whichever workbook is in front (risky in automation)
ThisWorkbook.Worksheets("Stock")       ' by name (safer than by index)
ws.Range("B2")                         ' by A1 address
ws.Cells(2, 2)                         ' by (row, column), good in loops
ws.Cells(ws.Rows.Count, "A").End(xlUp).Row   ' last used row in column A
ws.ListObjects("tblStock").DataBodyRange     ' an Excel Table body
```
Rules: qualify ranges with their worksheet (an unqualified `Range` means the *active* sheet); prefer `ThisWorkbook` for your own tool, and set object variables with `Set`.

### Example
```vba
Sub CountOpenLines()
    Dim ws As Worksheet, lastRow As Long
    Set ws = ThisWorkbook.Worksheets("PO_Lines")
    lastRow = ws.Cells(ws.Rows.Count, "A").End(xlUp).Row
    MsgBox "PO lines: " & lastRow - 1
End Sub
```
With a header in row 1 and data below, `lastRow - 1` is the number of data rows.

### In the news
See news box. Most "macro does nothing" cases for downloaded files are the Mark of the Web, not the code.

### Interview angle
> [!question] How it is asked
> "What is the difference between `ActiveWorkbook` and `ThisWorkbook`, and why does it matter?"

> [!tip] Strong answer includes
> - `ThisWorkbook` is where the code lives; `ActiveWorkbook` changes if the user switches windows or the macro opens another file
> - Always qualify ranges with a worksheet object
> - Use `End(xlUp)` or Tables for last row, not fixed numbers

---
## 4. Variables, Data Types and Option Explicit
> 🟡 Tier 3 · _Key points:_ Dim, Long vs Integer, Variant, Option Explicit, Const, Set

### Definition
Declare variables with `Dim name As Type`. Put `Option Explicit` at the top of every module (or enable Tools, Options, **Require Variable Declaration**) so a typo in a variable name raises a compile error instead of creating a new empty variable. Common types: `Long` (whole numbers; use it for row counts, since `Integer` overflows at 32,767 and Excel has over a million rows), `Double` (decimals), `String`, `Boolean`, `Date`, `Variant` (any type; slower), `Object` types such as `Worksheet`, `Range`, `Workbook`. Object variables need `Set`. `Const` defines a named constant.

### Example
```vba
Option Explicit

Const TAX_RATE As Double = 0.18

Sub LandedValue()
    Dim qty As Long, unitCost As Double, value As Double
    qty = 1250
    unitCost = 84.5
    value = qty * unitCost * (1 + TAX_RATE)
    Debug.Print "Value incl. tax: " & Format(value, "#,##0.00")
End Sub
```
`1250 × 84.5 × 1.18 = 124,637.50`, shown in the Immediate window (Ctrl+G).

### In the news
See news box.

### Interview angle
> [!question] How it is asked
> "Why use `Option Explicit` and `Long` instead of `Integer`?"

> [!tip] Strong answer includes
> - Catches typos at compile time
> - `Integer` is 16-bit and overflows on large row counts; `Long` is 32-bit
> - Declare object variables with `Set`; avoid `Variant` where speed matters

---
## 5. Control Flow: If, Select Case, For, For Each, Do While
> 🟡 Tier 3 · _Key points:_ If/ElseIf, Select Case, For Next, For Each, Do While, Exit For

### Definition
Branching: `If ... Then ... ElseIf ... Else ... End If` and `Select Case` for multiple discrete values. Loops: `For i = 1 To n ... Next i` (counted), `For Each cell In rng ... Next cell` (each object), `Do While cond ... Loop` (until a condition fails), `Exit For` / `Exit Do` to leave early. A loop over cells that writes to the sheet one cell at a time is slow; read the range into an array first (section 6).

### Example: ABC class label
```vba
Function AbcClass(cumPct As Double) As String
    Select Case cumPct
        Case Is <= 0.8: AbcClass = "A"
        Case Is <= 0.95: AbcClass = "B"
        Case Else: AbcClass = "C"
    End Select
End Function
```
Called from a sheet as `=AbcClass(F2)` (a user-defined function), cumulative percentage 0.72 returns "A", 0.9 returns "B", 0.99 returns "C" (the same cut-offs as ABC analysis in [[078 Excel for Operations & SCM]] and [[003 Inventory Management]]).

### In the news
See news box.

### Interview angle
> [!question] How it is asked
> "Write a macro to flag every row where stock is below the reorder point."

> [!tip] Strong answer includes
> - Loop from the first data row to the last row found with `End(xlUp)`
> - Compare two columns, write a flag to a third column
> - Mention doing it with a formula or conditional formatting if no macro is needed
> - Speed: read into an array and write back once

---
## 6. Fast, Reliable Range Code: Arrays, ScreenUpdating and Calculation
> 🟡 Tier 3 · _Key points:_ avoid Select, arrays, ScreenUpdating, Calculation manual, restore settings

### Definition
Three habits make macros fast:
1. **Avoid `Select`/`Activate`**; work with objects directly.
2. **Read a range into a Variant array, process in memory, write back once** (each cell access from VBA to the sheet is a slow call).
3. **Switch off screen redraw and automatic recalculation** during the run, and always restore them (including when an error occurs).

```vba
Sub FastClean()
    Dim ws As Worksheet, data As Variant, i As Long, lastRow As Long
    Set ws = ThisWorkbook.Worksheets("Stock")
    Application.ScreenUpdating = False
    Application.Calculation = xlCalculationManual
    On Error GoTo CleanUp                       ' always restore settings
    lastRow = ws.Cells(ws.Rows.Count, "A").End(xlUp).Row
    data = ws.Range("A2:C" & lastRow).Value      ' 2-D array (rows, columns)
    For i = 1 To UBound(data, 1)
        data(i, 1) = Trim(data(i, 1))            ' tidy material code
        If IsError(data(i, 3)) Then data(i, 3) = 0
    Next i
    ws.Range("A2:C" & lastRow).Value = data      ' write back once
CleanUp:
    Application.Calculation = xlCalculationAutomatic
    Application.ScreenUpdating = True
    If Err.Number <> 0 Then MsgBox "Error: " & Err.Description
End Sub
```

### Example
Cleaning 100,000 rows cell by cell can take minutes; the array version usually finishes in about a second or two. Timing differs by machine, so measure with `Timer` before and after (`t = Timer ... Debug.Print Timer - t`).

### In the news
See news box.

### Interview angle
> [!question] How it is asked
> "Your macro takes 10 minutes on 200,000 rows. How do you speed it up?"

> [!tip] Strong answer includes
> - Remove `Select`; use arrays; write back once
> - `ScreenUpdating = False`, manual calculation, and restore in a clean-up block
> - Consider Power Query or Python if the job is a transformation, not UI automation
> - Measure with `Timer` rather than guessing

---
## 7. Procedures, Functions and User-Defined Functions
> 🟡 Tier 3 · _Key points:_ Sub vs Function, ByVal vs ByRef, UDFs, Optional, modular code

### Definition
A `Sub` performs actions and returns nothing; a `Function` returns a value and can be called from a worksheet cell as a **UDF**. Arguments pass **ByRef** (the default: the procedure can change the caller's variable) or **ByVal** (a copy). A UDF called from a cell cannot change other cells or the Excel environment (it can only return its value). Split long macros into small named procedures that each do one job, and put shared helpers in one module.

### Example: safety stock UDF
```vba
Function SafetyStock(z As Double, sigmaD As Double, leadTime As Double) As Double
    SafetyStock = z * sigmaD * Sqr(leadTime)
End Function
```
`=SafetyStock(1.65, 10, 9)` returns `1.65 × 10 × 3 = 49.5` (the worked example in [[003 Inventory Management]]). The built-in alternative is the formula `=1.65*10*SQRT(9)`; a UDF is justified only when the logic is long or reused in many places. UDFs are not available in Excel on the web and are slower than native formulas.

### In the news
See news box.

### Interview angle
> [!question] How it is asked
> "What can a UDF not do compared with a Sub?"

> [!tip] Strong answer includes
> - A UDF in a cell returns a value only; it cannot modify other cells, formats or the workbook
> - ByVal vs ByRef difference
> - Prefer native formulas when they exist (faster, work everywhere)

---
## 8. Error Handling and Defensive Code
> 🟡 Tier 3 · _Key points:_ On Error GoTo, Err object, validation, cleanup, avoiding On Error Resume Next

### Definition
Runtime errors (file not found, sheet missing, divide by zero) stop a macro. Handle them with `On Error GoTo Label`, inspect `Err.Number` and `Err.Description`, clean up, and exit through a single path. Avoid blanket `On Error Resume Next` (it hides bugs); if you use it, scope it to one statement and reset with `On Error GoTo 0`. Validate inputs first (does the sheet exist, is the range empty, did the user cancel a dialog).

```vba
Function SheetExists(nm As String) As Boolean
    Dim ws As Worksheet
    On Error Resume Next
    Set ws = ThisWorkbook.Worksheets(nm)
    On Error GoTo 0
    SheetExists = Not ws Is Nothing
End Function

Sub SafeRun()
    On Error GoTo Fail
    If Not SheetExists("Stock") Then Err.Raise vbObjectError + 1, , "Sheet 'Stock' not found"
    ' ... work ...
    Exit Sub
Fail:
    MsgBox "Failed: " & Err.Description, vbExclamation
End Sub
```
Add a `Debug.Print` log or write a log row so failures are traceable.

### Example
A month-end macro merges 12 plant files. One file is open elsewhere and cannot be read. With handling, the macro logs "Plant 7 file locked", continues with the rest and reports 11 of 12 merged; without it, the macro stops at plant 7 with a debug prompt and a half-merged sheet.

### In the news
See news box.

### Interview angle
> [!question] How it is asked
> "How do you make a macro robust for other users?"

> [!tip] Strong answer includes
> - Input validation before work starts, and clear messages
> - `On Error GoTo` handler that restores application settings
> - Logging, and a test on copies of real data
> - Not using `On Error Resume Next` globally

---
## 9. Automating Files: Import and Consolidate a Folder of CSVs
> 🟡 Tier 3 · _Key points:_ Dir loop, Workbooks.Open, copy to master, close, headers once

### Definition
A standard operations automation: loop over the CSV exports in a folder, open each one, append its data to a master sheet, close it. Use `Dir` (or `FileSystemObject`) to list files, open them **read-only**, copy values with `.Value` assignment, and add the file name as a source column for traceability.

### Example
```vba
Sub ConsolidateCsv()
    Dim folder As String, f As String, wb As Workbook
    Dim master As Worksheet, nextRow As Long, lastRow As Long
    folder = "C:\Data\PlantExports\"                      ' set your folder, trailing backslash
    Set master = ThisWorkbook.Worksheets("Master")
    master.Cells.ClearContents
    nextRow = 1
    Application.ScreenUpdating = False
    f = Dir(folder & "*.csv")
    Do While f <> ""
        Set wb = Workbooks.Open(folder & f, ReadOnly:=True)
        With wb.Worksheets(1)
            lastRow = .Cells(.Rows.Count, "A").End(xlUp).Row
            If nextRow = 1 Then                            ' copy header from the first file
                master.Range("A1").Resize(1, .UsedRange.Columns.Count).Value = _
                    .Range("A1").Resize(1, .UsedRange.Columns.Count).Value
                nextRow = 2
            End If
            If lastRow >= 2 Then
                master.Cells(nextRow, 1).Resize(lastRow - 1, .UsedRange.Columns.Count).Value = _
                    .Range("A2").Resize(lastRow - 1, .UsedRange.Columns.Count).Value
                master.Cells(nextRow, .UsedRange.Columns.Count + 1).Resize(lastRow - 1, 1).Value = f
                nextRow = nextRow + lastRow - 1
            End If
        End With
        wb.Close SaveChanges:=False
        f = Dir()
    Loop
    Application.ScreenUpdating = True
    MsgBox "Rows loaded: " & nextRow - 2
End Sub
```
Pattern to remember: the file name column (`f`) lets you trace any row to its source. Test with two small files first. If all files share a layout, **Power Query's "From Folder" connector** does the same without code ([[075 Pivot Tables & Power Query]]).

### In the news
See news box. CSV files downloaded from the internet or e-mail may be blocked when they contain macros, but plain CSV data is read normally.

### Interview angle
> [!question] How it is asked
> "Plant teams send 15 Excel files every month. How would you consolidate them?"

> [!tip] Strong answer includes
> - Standardise the input template first
> - Loop over files, read-only, append, source-file column, log failures
> - Power Query "From Folder" as the no-code alternative
> - Reconciliation checks: row counts and totals against each source file

---
## 10. Report Automation: Split by Plant and Export PDF
> 🟡 Tier 3 · _Key points:_ AutoFilter, ExportAsFixedFormat, loop over unique values, naming files

### Definition
A frequent MIS task: take one master sheet and produce a file per plant (or per supplier). Approach: build a list of unique values in the key column, loop over them, filter the data, and export the visible sheet to PDF or copy the filtered rows to a new workbook. Mailing through Outlook can be added with the `Outlook.Application` object, but test with your own address first.

### Example
```vba
Sub ExportByPlant()
    Dim ws As Worksheet, plants As Object, p As Variant
    Dim lastRow As Long, i As Long, outPath As String
    Set ws = ThisWorkbook.Worksheets("Report")
    outPath = ThisWorkbook.Path & "\"
    lastRow = ws.Cells(ws.Rows.Count, "A").End(xlUp).Row
    Set plants = CreateObject("Scripting.Dictionary")           ' unique plant list
    For i = 2 To lastRow
        plants(ws.Cells(i, "A").Value) = 1                       ' column A = Plant
    Next i
    For Each p In plants.Keys
        ws.Range("A1").AutoFilter Field:=1, Criteria1:=p
        ws.ExportAsFixedFormat Type:=xlTypePDF, _
            Filename:=outPath & "Stock_" & p & ".pdf", _
            Quality:=xlQualityStandard, OpenAfterPublish:=False
    Next p
    ws.AutoFilterMode = False
End Sub
```
Set a print area and page setup (fit to one page wide) before exporting, and keep a copy of the unfiltered sheet. For 12 plants the macro writes 12 PDFs named by plant.

### In the news
See news box.

### Interview angle
> [!question] How it is asked
> "How would you automate a weekly report that must go to many recipients with only their own data?"

> [!tip] Strong answer includes
> - Master data plus a recipient list; loop, filter, export, send
> - Security: each recipient sees only their slice; log what was sent
> - Review step before sending; test addresses
> - Alternatives: Power BI row-level security, Power Automate for e-mail

---
## 11. Events and User Forms
> 🟡 Tier 3 · _Key points:_ Worksheet_Change, Workbook_Open, UserForm, Application.EnableEvents

### Definition
**Events** run code automatically: `Workbook_Open`, `Worksheet_Change`, `Worksheet_SelectionChange`, `Workbook_BeforeSave`. Code goes in the sheet or `ThisWorkbook` object, not a standard module. Inside an event that changes cells, set `Application.EnableEvents = False` first (to avoid the event calling itself) and restore it. **UserForms** (Insert, UserForm) give input dialogs with text boxes, combo boxes and buttons; use them for controlled data entry such as goods-receipt logs, but prefer **data validation** and **Tables** if they are enough.

### Example: timestamp when a stock quantity changes
```vba
Private Sub Worksheet_Change(ByVal Target As Range)
    If Intersect(Target, Me.Range("C2:C1000")) Is Nothing Then Exit Sub
    Application.EnableEvents = False
    Me.Cells(Target.Row, "F").Value = Now          ' column F = last updated
    Application.EnableEvents = True
End Sub
```
If the code errors before restoring events, Excel stops reacting; include an error handler that resets `EnableEvents = True`.

### In the news
See news box.

### Interview angle
> [!question] How it is asked
> "How would you log who changed a value and when?"

> [!tip] Strong answer includes
> - `Worksheet_Change` with `EnableEvents` handling
> - Writing to a log sheet (user from `Environ("USERNAME")`, old and new value if captured)
> - Limits: cannot capture the old value without extra code, and shared or web workbooks behave differently
> - Mention a database or SharePoint list when an audit trail is a real requirement

---
## 12. Security: Macros, Trust and Distribution
> 🟡 Tier 3 · _Key points:_ Mark of the Web, Trusted Locations, digital signatures, .xlam add-ins, no secrets in code

### Definition
Macros are executable code, so Office restricts them. Macro settings: disabled with notification, disabled except digitally signed, enabled (not recommended). Since the 2022-23 change, macros in **internet-origin** files are blocked until the file is unblocked or placed in a **Trusted Location**. Safer ways to share your tools: **digitally sign** the project with a code-signing certificate, distribute as an **add-in (.xlam)** from a trusted network path, or move logic to Power Query/Office Scripts. Never hard-code passwords or API keys in VBA; never run macros from unknown senders; keep a version of the file without macros for people who only need the data.

### Example
A team e-mails an .xlsm tool and half the staff cannot run it. Fix: put it on a shared drive that IT adds as a Trusted Location, or sign it, instead of telling everyone to lower macro security.

### In the news
See news box for the Mark-of-the-Web change and how to unblock a file you trust.

### Interview angle
> [!question] How it is asked
> "A manager asks you to email a macro workbook to 50 people. What are the concerns?"

> [!tip] Strong answer includes
> - Macros from e-mail/internet are blocked by default; trusted locations, signing or add-in distribution
> - Not lowering security settings; code review and version control
> - Alternatives that avoid macros (Power Query, Office Scripts, Power BI)
> - Data protection: no personal or confidential data in shared macro workbooks

---
## 13. ⭐ Advanced: Alternatives and the Modern Automation Stack
> ⭐ Advanced · _Added beyond the tracker_

### Definition
A modern analyst chooses among:
- **Power Query**: no-code repeatable import/transform; the first choice for data preparation ([[075 Pivot Tables & Power Query]]).
- **Office Scripts + Power Automate**: TypeScript scripts run on Excel on the web and can be triggered by flows (e-mail arrival, schedule through a flow); good for cloud-hosted workbooks.
- **Python**: via a notebook or script for heavy cleaning, statistics and forecasting ([[046 Python for Operations]], [[186 Python Data Cleaning & EDA Playbook]]); Excel's built-in Python feature is a Microsoft 365 option, so check availability in your tenant.
- **Excel formulas and dynamic arrays**: `FILTER`, `LET`, `XLOOKUP` ([[074 Array & Dynamic Array Functions]]) remove many VBA needs.
- **VBA**: still the tool for desktop UI automation and legacy workbooks.

Office Scripts example (TypeScript, runs in Excel on the web):
```typescript
function main(workbook: ExcelScript.Workbook) {
  const sheet = workbook.getActiveWorksheet();
  const header = sheet.getRange("A1:F1");
  header.getFormat().getFont().setBold(true);
  header.getFormat().getFill().setColor("#DDEBF7");
}
```
This does the same job as the `FormatHeader` macro in section 2.

### Example
Migration plan for a legacy macro workbook: (1) document what each macro does; (2) move data preparation to Power Query; (3) replace per-row loops with formulas or Python; (4) keep a small VBA layer only for PDF export and e-mail, or replace it with a Power Automate flow; (5) retire the macro file from e-mail distribution and put the tool on SharePoint with version history. Link the result to your KPI definitions ([[047 MIS & Dashboard Design]]) and checks ([[188 Financial Modelling in Excel]], [[187 Excel Interview Problem Bank & Case Exercises]]).

### In the news
See news box: Microsoft's documentation positions Office Scripts as the web-first, Power Automate-integrated alternative to desktop VBA, and the macro-blocking default makes distribution of VBA tools harder.

### Interview angle
> [!question] How it is asked
> "Our team has 40 legacy macro workbooks. How would you modernise them?"

> [!tip] Strong answer includes
> - Inventory and risk-rank them; keep what is critical, retire what is duplicate
> - Move data preparation to Power Query, analytics to Python, orchestration to Power Automate
> - Governance: version control, owners, documentation, testing, trusted distribution
> - Be honest that VBA stays for desktop-only tasks, and plan for people who maintain it

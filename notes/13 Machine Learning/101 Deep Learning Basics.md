---
tags: [machine-learning, tier3]
area: Machine Learning
topic: "Deep Learning Basics"
tier: Tier 3
roles: PM / Operations
status: complete
subtopics: 12
---
# Deep Learning Basics

⬅ [[100 ML for Product Management]] · [[_Index - Machine Learning|Machine Learning]] · [[218 Forecasting with ML & Foundation Models]] ➡
> **Area:** Machine Learning · **Priority:** 🟡 Tier 3 · **Target roles:** PM / Operations

## Sub-topics in this note
1. [[#1. Neural Network Architecture]]
2. [[#2. Activation Functions]]
3. [[#3. Forward & Backpropagation]]
4. [[#4. Optimizers]]
5. [[#5. Loss Functions]]
6. [[#6. Convolutional Neural Networks (CNN)]]
7. [[#7. Recurrent Neural Networks (RNN/LSTM)]]
8. [[#8. Transfer Learning]]
9. [[#9. Transformer & Attention]]
10. [[#10. Frameworks]]
11. [[#11. ⭐ Advanced: Overfitting, Regularization and Evaluation of Deep Models]]
12. [[#12. ⭐ Advanced: Generative AI and LLM Use Cases in Operations]]

## 📰 News box
> [!news] Shared news hook for this topic (2024–2026): foundation-style models enter supply chains
> **Amazon's foundational forecasting model (11 Jun 2025).** Amazon described a "foundational AI forecasting model" trained on sales history plus signals such as weather and holidays, predicting demand for hundreds of millions of products a day; it reported a **10% gain in long-term national forecasts for deal events and 20% in regional forecasts** for millions of popular items, live in the US, Canada, Mexico and Brazil. The same announcement created an agentic-AI team in Amazon Robotics for robots that follow natural-language instructions. ([About Amazon](https://www.aboutamazon.com/news/operations/amazon-ai-innovations-delivery-forecasting-robotics))
> 
> **MuleHunter.AI (RBI Innovation Hub).** AI/ML pattern detection for mule accounts; reported live across 31 banks (Sept 2026 write-up). ([RMA India](https://rmaindia.org/mulehunter-ai-rbis-ai-fraud-detection-system-now-live-across-31-banks/))
> 
> Sub-topics that say **"See news box"** reuse these items. Amazon's page does not state the model's architecture, so do not claim it is a transformer in an interview.

---
## 1. Neural Network Architecture
> 🟡 Tier 3 · _Tracker hint:_ Input layer → Hidden layers → Output; neurons, weights, biases; matrix multiplication

### Definition
A neural network is a stack of layers; each layer applies a linear map followed by a non-linear activation.

For one layer: $\mathbf a^{(l)}=f\!\left(W^{(l)}\mathbf a^{(l-1)}+\mathbf b^{(l)}\right)$, where $W$ holds the **weights**, $\mathbf b$ the **biases**, $f$ the activation.

- **Input layer:** features (e.g., 20 demand drivers).
- **Hidden layers:** learn intermediate representations; "deep" means many.
- **Output layer:** prediction (1 neuron for regression/binary, *K* for multi-class).

Parameter count for a dense layer with $n_{in}$ inputs and $n_{out}$ neurons = $n_{in}\times n_{out}+n_{out}$. Because the whole batch is multiplied as matrices, GPUs speed it up. Without non-linear activations, stacked layers collapse into one linear model. By the **universal approximation theorem**, a wide enough single hidden layer can approximate any continuous function, but depth is more parameter-efficient.

For tabular business data, gradient boosting often still beats neural nets; deep learning wins on images, text, audio and very large data.

### Example
Network 10 → 16 → 8 → 1. Parameters: (10×16+16) + (16×8+8) + (8×1+1) = 176 + 136 + 9 = **321**. A single forward pass of one row: matrices 16×10, 8×16, 1×8.

### In the news
See news box. Amazon's forecasting model is a large-scale neural approach to what was once ARIMA per series; the architecture is not disclosed on the page.

### Interview angle
> [!question] How it is asked
> "Explain a neural network to a non-technical manager." or "Why do we need hidden layers?"

> [!tip] Strong answer includes
> - Layers, weights, biases, activation in plain language (weighted sum then a squash)
> - Why non-linearity matters
> - Parameter count intuition and overfitting risk
> - When not to use deep learning (small tabular data, need for explainability)

---

## 2. Activation Functions
> 🟡 Tier 3 · _Tracker hint:_ ReLU (most common), Sigmoid (binary output), Softmax (multi-class), Tanh (RNN)

### Definition
Activations add non-linearity.

| Function | Formula | Range | Typical use |
|---|---|---|---|
| ReLU | $\max(0,x)$ | [0, ∞) | Hidden layers (default) |
| Leaky ReLU | $\max(0.01x,x)$ | (−∞, ∞) | Avoids "dead" neurons |
| Sigmoid | $\sigma(x)=\frac1{1+e^{-x}}$ | (0, 1) | Binary output probability |
| Tanh | $\frac{e^x-e^{-x}}{e^x+e^{-x}}$ | (−1, 1) | RNN/LSTM gates, zero-centred |
| Softmax | $\frac{e^{z_i}}{\sum_j e^{z_j}}$ | (0, 1), sums to 1 | Multi-class output |

Why ReLU: cheap, does not saturate for positive inputs, so gradients flow (reduces the **vanishing gradient** problem seen with sigmoid/tanh, whose derivative is at most 0.25 and 1 respectively). Regression output uses **no activation** (linear).

### Example
Softmax of logits (2, 1, 0): exponentials = 7.389, 2.718, 1.000; sum = 11.107. Probabilities = **0.665, 0.245, 0.090** (sum = 1.000). Sigmoid(0) = 0.5; sigmoid(2) = 1/(1+0.1353) = **0.881**.

### In the news
See news box. Fraud tools like MuleHunter.AI output a risk probability; for a binary risk score the final layer is typically a sigmoid.

### Interview angle
> [!question] How it is asked
> "Why is ReLU preferred over sigmoid in hidden layers?" or "Which activation for a 5-class output?"

> [!tip] Strong answer includes
> - Output-layer choice by task (linear, sigmoid, softmax)
> - Vanishing gradient explanation
> - Dying ReLU and the Leaky fix
> - Softmax as probabilities summing to 1

---

## 3. Forward & Backpropagation
> 🟡 Tier 3 · _Tracker hint:_ Forward: compute predictions; Backward: compute gradients; update weights by gradient descent

### Definition
**Forward pass:** push inputs through layers to get prediction $\hat y$, then compute loss $L(\hat y,y)$.

**Backpropagation:** apply the **chain rule** from output back to input to compute $\partial L/\partial w$ for every weight, reusing intermediate results efficiently.

**Gradient descent update:** $w\leftarrow w-\eta\,\frac{\partial L}{\partial w}$ where $\eta$ is the learning rate.

For a single neuron $\hat y=\sigma(wx+b)$ with squared loss $L=\tfrac12(\hat y-y)^2$:
$$\frac{\partial L}{\partial w}=(\hat y-y)\,\sigma'(z)\,x,\qquad \sigma'(z)=\hat y(1-\hat y)$$
Training loops over **epochs** and **mini-batches**. Problems: vanishing/exploding gradients (fixed with ReLU, good initialisation such as He/Xavier, normalisation, residual connections, gradient clipping).

### Example
One linear neuron $\hat y=wx$, $x=2$, $w=1$, target $y=6$, $L=\tfrac12(\hat y-y)^2$. Forward: $\hat y=2$, $L=\tfrac12(4)^2=8$. Gradient: $(\hat y-y)x=(2-6)(2)=-8$. With $\eta=0.1$: $w=1-0.1(-8)=1.8$. New $\hat y=3.6$, $L=\tfrac12(2.4)^2=2.88$. Loss fell from 8 to 2.88.

### In the news
See news box. Training a model like Amazon's forecaster means running this forward-backward loop over enormous history; only the principle, not the details, is public.

### Interview angle
> [!question] How it is asked
> "Explain backpropagation in simple words."

> [!tip] Strong answer includes
> - Forward = predict and measure error; backward = assign blame via chain rule
> - Gradient descent step with learning rate
> - Too high/low learning rate behaviour
> - Vanishing gradient awareness

---

## 4. Optimizers
> 🟡 Tier 3 · _Tracker hint:_ SGD (stochastic), Adam (adaptive, most popular), RMSprop; learning rate scheduling

### Definition
Optimisers decide *how* to use gradients $g_t$.

- **SGD (mini-batch):** $w\leftarrow w-\eta g$. Simple; noisy; **momentum** adds a velocity term $v\leftarrow\beta v+g$ to smooth.
- **RMSprop:** divides by a running average of squared gradients: $w\leftarrow w-\frac{\eta}{\sqrt{s}+\epsilon}g$, adapting the step per parameter.
- **Adam:** combines momentum ($m$) and RMSprop ($v$) with bias correction: $w\leftarrow w-\eta\frac{\hat m}{\sqrt{\hat v}+\epsilon}$; defaults $\beta_1=0.9,\ \beta_2=0.999,\ \eta=10^{-3}$. Fast, robust default.
- **AdamW:** decoupled weight decay, the common choice for transformers.

**Learning-rate scheduling:** step decay, cosine annealing, warm-up (small LR first), reduce-on-plateau. Large batch plus scheduled LR generally trains faster; SGD with momentum sometimes generalises better for CNNs.

```python
import torch
opt = torch.optim.Adam(model.parameters(), lr=1e-3)
sched = torch.optim.lr_scheduler.CosineAnnealingLR(opt, T_max=50)
```

### Example
SGD with $\eta=0.1$ and gradient 5 changes a weight by −0.5. Adam on the same parameter with gradients consistently around 5 normalises: $\hat m/\sqrt{\hat v}\approx1$, so the step ≈ $\eta\times1$ = 0.001 at default LR; a parameter with tiny gradients (0.001) gets a similar-sized step, which is the "adaptive" benefit.

### In the news
See news box. Large-scale production models like those behind forecasting or fraud scoring are typically trained with adaptive optimisers, but companies rarely disclose which.

### Interview angle
> [!question] How it is asked
> "Why is Adam the default? When might SGD be better?"

> [!tip] Strong answer includes
> - Momentum and adaptive scaling intuition
> - Typical hyperparameters and LR schedule
> - Trade-off: speed vs generalisation
> - LR as the most important hyperparameter

---

## 5. Loss Functions
> 🟡 Tier 3 · _Tracker hint:_ MSE (regression), Cross-Entropy (classification), Huber (robust regression)

### Definition
The loss measures prediction error; training minimises it.

- **MSE:** $\frac1n\sum(y-\hat y)^2$. Penalises large errors heavily; sensitive to outliers.
- **MAE:** $\frac1n\sum|y-\hat y|$. Robust, gradient constant.
- **Huber:** quadratic for small errors ($|e|\le\delta$: $\tfrac12e^2$), linear for large ($\delta(|e|-\tfrac12\delta)$). Best of both.
- **Binary cross-entropy:** $-\frac1n\sum[y\log\hat p+(1-y)\log(1-\hat p)]$.
- **Categorical cross-entropy:** $-\sum_k y_k\log\hat p_k$.
- **Quantile (pinball) loss** for forecast intervals; **focal loss** for imbalance.

Match loss to business cost: if stock-outs cost more than excess, use an asymmetric/quantile loss.

### Example
Actual (100, 110, 300), predicted (102, 108, 120). Errors: 2, 2, 180. MSE = (4+4+32,400)/3 = **10,802.7**; MAE = 184/3 = **61.3**. One outlier dominates MSE. Binary CE for true y=1, predicted p=0.9: −ln 0.9 = **0.105**; if p=0.1: −ln 0.1 = **2.303**.

### In the news
See news box. A national forecasting model is usually judged by percentage accuracy gains (Amazon's 10% and 20%), but trained on a differentiable loss; picking that loss to reflect business cost is a modelling decision.

### Interview angle
> [!question] How it is asked
> "Which loss would you use for demand forecasting? For fraud classification?"

> [!tip] Strong answer includes
> - MSE/MAE/Huber trade-offs with outliers
> - Cross-entropy for probabilities
> - Business-aligned/asymmetric loss and metrics separate from the loss
> - Imbalance handling (weights, focal)

---

## 6. Convolutional Neural Networks (CNN)
> 🟡 Tier 3 · _Tracker hint:_ Conv layers extract features; pooling for downsampling; image recognition, quality inspection

### Definition
CNNs exploit the spatial structure of images using small **filters (kernels)** slid across the image, sharing weights, so far fewer parameters than dense layers and translation tolerance.

- **Convolution layer:** each filter produces a feature map (edges → textures → parts → objects as depth grows).
- **Pooling (max/average):** downsample, add robustness.
- **Fully connected / global-average-pool head:** classification.

Output size: $\left\lfloor\frac{W-K+2P}{S}\right\rfloor+1$ for input $W$, kernel $K$, padding $P$, stride $S$. Parameters per conv layer = $(K\times K\times C_{in}+1)\times C_{out}$.

Architectures: LeNet, VGG, ResNet (skip connections), EfficientNet; detection: YOLO, Faster R-CNN; segmentation: U-Net. Operations uses: visual quality inspection, package damage, shelf monitoring, reading labels, crop-disease detection.

### Example
Input 28×28, kernel 3×3, stride 1, no padding → (28−3)/1+1 = **26×26**. With 32 filters on 1 input channel: params = (3×3×1+1)×32 = **320**. Max-pool 2×2 stride 2 → 13×13.

### In the news
See news box. Amazon Robotics' warehouse systems combine vision with robot control; its June 2025 plan adds language-instructed robot behaviours.

### Interview angle
> [!question] How it is asked
> "How would you automate quality inspection on a production line?"

> [!tip] Strong answer includes
> - CNN idea in one line (learned filters detect patterns), pooling
> - Data needs and transfer learning
> - Metrics (recall for defects), edge deployment, lighting variation
> - Business case: inspection cost and defect leakage

---

## 7. Recurrent Neural Networks (RNN/LSTM)
> 🟡 Tier 3 · _Tracker hint:_ Sequential data; LSTM handles vanishing gradient; demand forecasting, NLP

### Definition
An **RNN** processes a sequence step by step, carrying a **hidden state**: $h_t=\tanh(W_hh_{t-1}+W_xx_t+b)$. Training uses backpropagation through time; repeated multiplication shrinks or explodes gradients (**vanishing gradient**), so basic RNNs forget long-range patterns.

**LSTM** adds a **cell state** and gates:
- forget gate $f_t$ (what to erase), input gate $i_t$ (what to write), output gate $o_t$ (what to expose);
- $c_t=f_t\odot c_{t-1}+i_t\odot\tilde c_t$, so information can pass almost unchanged, easing gradient flow.

**GRU** is a lighter variant. Uses: demand/energy forecasting, sensor sequences, speech, text. Today, **transformers** have replaced RNNs for most NLP and many forecasting tasks, but LSTMs remain for small streaming problems. Note for forecasting: well-tuned gradient boosting often matches LSTMs on retail data.

### Example
Sequence of weekly sales fed with a 4-week window: input shape (batch, 4, 1). An LSTM with 32 units has parameters $4\times(32\times(32+1)+32)=4\times1088=$ **4,352**.

### In the news
See news box. Amazon's forecasting uses weather and holiday signals; sequence models are one way to ingest such time-dependent inputs (architecture not disclosed).

### Interview angle
> [!question] How it is asked
> "Why LSTM instead of a plain RNN?" or "Would you use an LSTM for demand forecasting?"

> [!tip] Strong answer includes
> - Hidden state and vanishing gradient
> - Gates intuition
> - Baselines first; compare with GBM/ARIMA
> - Mention transformers as the modern default

---

## 8. Transfer Learning
> 🟡 Tier 3 · _Tracker hint:_ Pre-trained model (ResNet, BERT) fine-tuned on your data; less data needed

### Definition
Reuse a model trained on a large dataset (ImageNet, web text) for your task.

- **Feature extraction:** freeze the backbone, train only a new head.
- **Fine-tuning:** unfreeze some or all layers at a small learning rate.
- **Domain adaptation:** adjust to a different distribution.

Why it works: early layers learn general features (edges, syntax). Benefits: far less labelled data, faster training, better accuracy. Risks: domain mismatch, licence and bias inherited from the base model, catastrophic forgetting.

```python
import torch, torchvision
m = torchvision.models.resnet18(weights="DEFAULT")
for p in m.parameters(): p.requires_grad = False
m.fc = torch.nn.Linear(m.fc.in_features, 3)   # 3 defect classes
```

### Example
Defect inspection with only 500 labelled images: training from scratch might reach 70% accuracy; fine-tuning a pre-trained ResNet on the same 500 typically does much better (illustrative; verify on your data). Rule: aim for hundreds, not millions, of examples.

### In the news
See news box. "Foundation" style models, trained once then adapted, are the same logic as transfer learning: Amazon calls its forecaster "foundational".

### Interview angle
> [!question] How it is asked
> "We have only 1,000 labelled images. How would you build a classifier?"

> [!tip] Strong answer includes
> - Pre-trained backbone, replace head, freeze then fine-tune
> - Augmentation and validation strategy
> - Data quality over quantity
> - Cost and time saving vs building from scratch

---

## 9. Transformer & Attention
> 🟡 Tier 3 · _Tracker hint:_ Self-attention mechanism; BERT, GPT architecture; NLP revolution; SCM contract analysis

### Definition
The **transformer** (Vaswani et al., 2017, "Attention Is All You Need") processes all tokens in parallel using **self-attention**: each token forms a query $Q$, key $K$ and value $V$ and attends to all others.

$$\text{Attention}(Q,K,V)=\text{softmax}\!\left(\frac{QK^{T}}{\sqrt{d_k}}\right)V$$

- **Multi-head attention** learns several relationships at once; **positional encodings** give order; residual connections and layer norm stabilise training.
- **BERT:** encoder-only, bidirectional; good for classification, NER, search (understanding).
- **GPT:** decoder-only, predicts the next token; good for generation (LLMs).
- Cost: attention is $O(n^2)$ in sequence length.

In operations: contract and invoice extraction, supplier-news monitoring, chatbots over SOPs, time-series transformers, and agentic workflows. Cautions: hallucination, data privacy, evaluation.

### Example
Sentence: "The supplier delayed the shipment because it was damaged." Attention lets the token "it" weight "shipment" more than "supplier" (resolving the reference). Scaling: with $d_k=64$, scores are divided by $\sqrt{64}=8$ to keep softmax from saturating.

### In the news
See news box. Amazon's robotics agentic-AI team (language-instructed robots) is a transformer-era idea applied to warehouses; MuleHunter.AI is not stated to be a transformer.

### Interview angle
> [!question] How it is asked
> "What is attention and why did transformers replace RNNs?" or "How can LLMs help in supply chain?"

> [!tip] Strong answer includes
> - Self-attention in plain words and parallelism advantage
> - BERT vs GPT distinction
> - Concrete SCM use cases (contracts, RFQs, planner copilots)
> - Limits: hallucination, cost, data confidentiality

---

## 10. Frameworks
> 🟡 Tier 3 · _Tracker hint:_ TensorFlow/Keras (production-friendly), PyTorch (research-friendly), Scikit-learn (classical ML)

### Definition
| Framework | Strength | Use |
|---|---|---|
| **scikit-learn** | Clean API for classical ML (regression, trees, SVM, clustering, preprocessing, pipelines) | Tabular problems, baselines |
| **TensorFlow/Keras** | High-level Keras, TF Serving, TFLite for mobile/edge | Production deployment |
| **PyTorch** | Pythonic, dynamic graphs, dominant in research and LLMs | Prototyping, modern DL |
| **XGBoost/LightGBM** | Gradient boosting | Best on many tabular tasks |
| **Hugging Face Transformers** | Pre-trained NLP/vision models | Fine-tuning |

Both TF and PyTorch have mature production paths today (ONNX, TorchServe), so the "production vs research" split is a rule of thumb.

```python
from tensorflow import keras
model = keras.Sequential([
    keras.layers.Dense(16, activation="relu", input_shape=(10,)),
    keras.layers.Dense(1)])
model.compile(optimizer="adam", loss="mse")
model.fit(X, y, epochs=20, batch_size=32, validation_split=0.2)
```

### Example
Task: predict machine failure from 20 sensor columns, 50,000 rows: start with scikit-learn logistic regression, then XGBoost; use PyTorch/Keras only if you add raw waveform data or need a neural model.

### In the news
See news box. Frameworks matter less than data and process; large firms standardise on one stack for deployment.

### Interview angle
> [!question] How it is asked
> "Which tools would you use to build this model?"

> [!tip] Strong answer includes
> - Choose by problem (tabular → sklearn/XGBoost; images/text → PyTorch/Keras)
> - Simple baseline first
> - Deployment considerations (latency, monitoring)
> - You need not be a coder as a PM/consultant; know the vocabulary and trade-offs

---

## 11. ⭐ Advanced: Overfitting, Regularization and Evaluation of Deep Models
> ⭐ Advanced · _Added beyond the tracker_

### Definition
Deep models can memorise training data. Signs: training loss falls while validation loss rises.

Controls: **more data/augmentation**, **dropout** (randomly zero units with probability $p$ during training), **L2 weight decay**, **early stopping** on validation loss, **batch normalisation**, smaller model, ensembling.

Evaluation discipline: train/validation/test split (time-based for time series), **hyperparameter tuning** on validation only, final one-time test; monitor **drift** after deployment. Use baselines and learning curves. Interpretability: SHAP, saliency (Grad-CAM for CNNs).

### Example
Epoch 10: train loss 0.20, val loss 0.25. Epoch 30: train 0.05, val 0.40. Best epoch is near 10; early stopping with patience 5 would stop around epoch 15 and restore epoch-10 weights.

### In the news
See news box. Production claims such as "20% better regional forecasts" are meaningful only when measured on held-out data and compared with a baseline.

### Interview angle
> [!question] How it is asked
> "Your model has 99% training accuracy but 70% in production. What happened?"

> [!tip] Strong answer includes
> - Overfitting vs data leakage vs drift
> - Regularisation tools and proper validation
> - Monitoring and retraining
> - Business metric validation

---

## 12. ⭐ Advanced: Generative AI and LLM Use Cases in Operations
> ⭐ Advanced · _Added beyond the tracker_

### Definition
LLMs are transformer models trained on huge text corpora. Useful patterns:

- **Prompting / few-shot** classification and extraction (invoices, contracts, emails).
- **RAG (retrieval-augmented generation):** retrieve relevant documents (SOPs, policies, contracts) and have the LLM answer from them, reducing hallucination and keeping knowledge current.
- **Copilots/agents:** query planning data in natural language, draft supplier emails, trigger actions through tools with human approval.
- **Evaluation:** accuracy on a labelled set, groundedness, cost per query, latency, safety.

Risks: hallucination, confidentiality (use enterprise deployments), prompt injection, regulatory/DPDP concerns, over-trust.

### Example
A planner asks, "Which SKUs at risk of stock-out next week?" An LLM agent runs a SQL query on the planning database, summarises top 10 SKUs and drafts expedite emails; the planner approves. If this saves 30 minutes per planner per day for 40 planners over 250 days: 30/60 × 40 × 250 = **5,000 hours/year**.

### In the news
See news box. Amazon's June 2025 robotics announcement (natural-language robot instructions) shows agentic AI moving from software into physical operations.

### Interview angle
> [!question] How it is asked
> "How would you use generative AI in our supply chain team?"

> [!tip] Strong answer includes
> - Pick high-volume, low-risk text tasks first
> - RAG and human-in-the-loop, guardrails
> - Metrics: time saved, accuracy, adoption
> - Data security and governance

---
## 🔗 Go deeper: expansion notes
- [[219 NLP, Embeddings & LLM Applications for Analysts|NLP, Embeddings & LLM Applications for Analysts]]
- [[218 Forecasting with ML & Foundation Models|Forecasting with ML & Foundation Models]]

# ML Learning Journey & Projects 🚀

This repository documents my journey to becoming a job-ready AI/ML Engineer. It contains a disciplined 24-week study plan, interview preparation notes (focusing on LLMs, RAG, and Fine-tuning), and the actual projects I am building along the way.

---

## 🤖 Daily Study Assistant

I have built a custom automation tool to manage my 24-week learning schedule.

### Setup
1.  **Configure**: Edit `config.json` with your start date and email.
2.  **Run**:
    ```bash
    python3 daily_assistant.py
    ```
3.  **Result**: The script sends me a daily agenda email and automatically opens the relevant `README.md` and my notes file for the day.

---

## 📂 Project & Curriculum Index

### Supervised Learning Projects
*   **[Incident Risk Prediction](./Phase_01_Foundations/Week_03_Core_ML/Supervised/Linear%20Regression/Incident_Risk_Prediction)**
    *   **Goal:** Predict the "Risk Score" of ServiceNow incidents to prevent escalations.
    *   **Tech:** Multiple Linear Regression, Synthetic Data Generation, Data Cleaning.
    *   **Key Learnings:** Handling dirty data, interpreting model coefficients for business value.
*   **[Linear Regression Project](./Phase_01_Foundations/Week_03_Core_ML/Supervised/Linear%20Regression/Linear_Regression_Project.ipynb)**
    *   Introductory notebook demonstrating the basics of Linear Regression.

### Phase 1: Foundations - Week 3 (Core ML)
I have implemented the following standard algorithms from scratch/sklearn to master the concepts:

**Supervised Learning**
*   [Logistic Regression](./Phase_01_Foundations/Week_03_Core_ML/Supervised/Logistic_Regression)
*   [Decision Trees](./Phase_01_Foundations/Week_03_Core_ML/Supervised/Decision_Trees)
*   [Random Forest](./Phase_01_Foundations/Week_03_Core_ML/Supervised/Random_Forest)
*   [SVM](./Phase_01_Foundations/Week_03_Core_ML/Supervised/SVM)
*   [KNN](./Phase_01_Foundations/Week_03_Core_ML/Supervised/KNN)
*   [Naive Bayes](./Phase_01_Foundations/Week_03_Core_ML/Supervised/Naive_Bayes)
*   [Gradient Boosting](./Phase_01_Foundations/Week_03_Core_ML/Supervised/Gradient_Boosting)

**Unsupervised Learning**
*   [K-Means Clustering](./Phase_01_Foundations/Week_03_Core_ML/Unsupervised/K_Means_Clustering)
*   [Hierarchical Clustering](./Phase_01_Foundations/Week_03_Core_ML/Unsupervised/Hierarchical_Clustering)
*   [PCA](./Phase_01_Foundations/Week_03_Core_ML/Unsupervised/PCA)
*   [DBSCAN](./Phase_01_Foundations/Week_03_Core_ML/Unsupervised/DBSCAN)
*   [Anomaly Detection](./Phase_01_Foundations/Week_03_Core_ML/Unsupervised/Anomaly_Detection)

---

## 📅 The 24-Week Job-Ready Plan (AWS + GenAI)

**Goal:** Become job-ready in ~6 months with 3 hours of disciplined work daily.

**Daily Routine:**
*   60 min: Learn concept
*   90 min: Code / Build
*   30 min: Notes + Revision

### 🟢 PHASE 1: Foundations (The "ML-Ready" Stage)
| Week | Focus | deliverables |
| :--- | :--- | :--- |
| **1** | **Python for ML** | Repo `python-for-ml` (Clean code, NumPy/Pandas scripts). |
| **2** | **Math + ML Intuition** | House Price Predictor (From scratch + sklearn). Focus: Gradient Descent. |
| **3** | **Core ML** | Spam Classifier API (FastAPI). First backend exposure. |
| **4** | **ML → DL Bridge** | Neural Net from scratch (NumPy). Understanding Backprop. |

### 🔵 PHASE 2: Deep Learning Core
| Week | Focus | deliverables |
| :--- | :--- | :--- |
| **5** | **PyTorch** | MNIST Classifier (Proper structure, not just notebook). |
| **6** | **CNNs** | Image Classifier (Cats vs Dogs). Convolutions, Pooling, ResNet. |
| **7** | **RNN / LSTM** | Log Sequence Anomaly Detector. Time series basics. |
| **8** | **Model Engineering** | Modular Training Pipeline. Optimizers & Regularization. |

### 🔴 PHASE 3: Transformers & LLMs (The "Strong Profile" Stage)
| Week | Focus | deliverables |
| :--- | :--- | :--- |
| **9** | **Attention & Transformers** | Mini Transformer from scratch. Self-attention mechanism. |
| **10** | **HuggingFace** | Text Summarizer API. Tokenizers & Pretrained models. |
| **11** | **LLM Fine-Tuning** | Custom Domain Chatbot. LoRA & PEFT. |
| **12-13** | **🔥 Flagship Project #1** | **AI Document Intelligence System (AWS)**<br>Features: PDF Upload, Vector Search (RAG), Q&A.<br>Stack: AWS S3, EC2, Lambda, Pinecone/FAISS. |

### 🟣 PHASE 4: Diffusion Models (The "GenAI Differentiator")
| Week | Focus | deliverables |
| :--- | :--- | :--- |
| **14** | **Generative Models** | VAEs and GANs concepts. |
| **15** | **Diffusion Theory** | Understanding U-Net, CLIP, Noise→Image. |
| **16-17** | **🔥 Flagship Project #2** | **Stable Diffusion Platform (AWS + GPU)**<br>Features: Text-to-Image, Gallery, History.<br>Stack: AWS EC2 GPU (g4dn), S3, CloudFront. |

### 🟠 PHASE 5: Production & AWS
| Week | Focus | deliverables |
| :--- | :--- | :--- |
| **18** | **Docker + APIs** | Dockerize all previous services. |
| **19** | **AWS Deep Dive** | IAM, Cost Control, Lambda limits. |
| **20** | **CI/CD** | GitHub Actions for auto-deploy. |
| **21** | **Monitoring** | CloudWatch Logs & Dashboards. Drift detection. |
| **22** | **System Design** | Architecture diagrams, Scaling strategies. |

### 🟤 PHASE 6: Interview + Job Prep
| Week | Focus | deliverables |
| :--- | :--- | :--- |
| **23** | **System Design** | Mock interviews: "Design a Recommendation System". |
| **24** | **Career Polish** | Resume, GitHub cleanup, LinkedIn activity. |

---

## 🧠 Advanced AI Engineering (Interview Prep)

This section covers the "Edge Layer"—the difference between "I used GPT" and "I'm an AI Engineer."

![Fine-Tuning vs RAG](https://img.shields.io/badge/Strategy-RAG_vs_FineTuning-blue)

### 1. The "Big Truth" About Customizing LLMs
Most companies **do not** full fine-tune models. They use:
1.  **Prompt Engineering**
2.  **RAG (Retrieval-Augmented Generation)**
3.  **Light Fine-Tuning (LoRA/Adapters)**

**Golden Rule:**
> "In production, we start with **Prompting**, move to **RAG** for knowledge grounding, and only use **LoRA** when we need consistent behavior, style, or structured outputs."

### 2. Strategy Breakdown

#### A. RAG (The Industry Standard) ⭐
*   **What it does:** Retrieves relevant text chunks and injects them into the context window.
*   **Best for:** Adding **new facts**, ensuring **freshness**, and reducing hallucinations.
*   **When to fail:** When you need strict style consistency or complex reasoning patterns.

#### B. LoRA / PEFT (The Specialist) ⭐
*   **What it does:** Freezes the base model and trains tiny adapter layers.
*   **Best for:** **Style** (e.g., medical tone), **Format** (JSON, SQL), **Tool Calling**.
*   **Avoid for:** Injecting new knowledge (Model will hallucinate facts).

### 3. Interview "One-Liners" to Memorize
*   *"RAG solves knowledge freshness without retraining."*
*   *"LoRA adapts behavior cheaply without catastrophic forgetting."*
*   *"We evaluate fine-tuning by comparing base vs. adapter outputs on task-specific metrics."*
*   *"Prompting is fast but brittle at scale."*

### 4. Production Checklist
- [ ] **Data:** Collect high-quality instruction-response pairs.
- [ ] **Clean:** Format data for the specific model (e.g., ChatML).
- [ ] **Train:** Use LoRA to save cost (vs full finetuning).
- [ ] **Eval:** Validate against a hold-out set (Human + LLM-as-judge).
- [ ] **Monitor:** Watch for drift and cost-per-token.

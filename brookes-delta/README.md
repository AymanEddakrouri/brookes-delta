# Brookes' Δ Categorical Dispersion Calculator

[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Implementation of **Brookes' Measure of Categorical Dispersion (Δ)** for bibliometric analysis and science of science research. This tool quantifies the thematic concentration vs. dispersion of intellectual output in any research domain.

## 📊 What is Brookes' Δ?

Brookes' Δ is a statistical measure ranging from **0 to 1** that answers a critical question in bibliometrics:

- **Δ → 1.0**: High thematic concentration (specialized research)
- **Δ → 0.0**: High thematic dispersion (interdisciplinary research)

The measure was introduced by B.C. Brookes (1977) and provides a single, interpretable metric for comparing the thematic structure across journals, research fields, or institutional outputs.

## 🚀 Quick Start

### Installation
```bash
# Clone repository
git clone https://github.com/yourusername/brookes-delta.git
cd brookes-delta

# Install dependencies
pip install -r requirements.txt
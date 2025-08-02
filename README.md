🎨 SketchScape: Real vs. Sketch Detector

**SketchScape** is a deep learning-based image classifier that distinguishes between real photographs and sketch-style images. Built using Convolutional Neural Networks (CNN), this project aims to visually interpret and classify images through an interactive and intuitive Streamlit web application.

🚀 Features

- 📂 Handles clean separation of sketch and real image datasets
- 🔍 CNN-based model for robust image classification
- 🔎 Grad-CAM integration to visualize what the model "sees"
- 🌐 Streamlit UI for easy image uploads and live predictions
- 📊 CSV logging of prediction results
- 📁 Organized folder structure and modular Python scripts

🧠 Motivation

Real vs. Sketch image classification has practical use cases in:
- Digital art filtering
- Sketch-based image retrieval
- AI-powered content moderation

This project also serves as a foundational exercise in deploying computer vision models with an accessible UI.

🧰 Tech Stack

| Tool/Framework | Purpose                          |
|----------------|----------------------------------|
| Python         | Programming language             |
| TensorFlow/Keras | CNN model training             |
| OpenCV         | Image preprocessing              |
| Streamlit      | Web-based interface              |
| Grad-CAM       | Model interpretability           |
| Pandas         | Data manipulation and logging    |
| Matplotlib     | Visualizations                   |

🗂️ Folder Structure
│
├── data/
│ ├── train/
│ │ ├── real/
│ │ └── sketch/
│ └── test/
│ ├── real/
│ └── sketch/
│
├── model/
│ ├── cnn_model.h5
│ └── model_visualization.png
│
├── utils/
│ ├── preprocess.py
│ ├── gradcam.py
│ └── evaluate.py
│
├── app/
│ └── streamlit_app.py
│
├── screenshots/
│ └── sample_output.png
│
├── requirements.txt
└── README.md


🔧 Setup & Installation
**Clone the repository**

git clone https://github.com/Akkkkkkansha/sketchscape.git
cd sketchscape

Create a virtual environment
python -m venv venv
.\venv\Scripts\activate      # For Windows
source venv/bin/activate    # For Mac/Linux

Install dependencies
pip install -r requirements.txt

Run the app
streamlit run app/streamlit_app.py


📜 License
This project is licensed under the MIT License – see the [LICENSE](./LICENSE) file for details.



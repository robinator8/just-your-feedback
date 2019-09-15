import PIL

from imageai.Prediction import ImagePrediction
from imageai.Prediction.Custom import ModelTraining

model_trainer = ModelTraining()

model_trainer.setModelTypeAsSqueezeNet()
model_trainer.setDataDirectory(r"C:\Users\Adrian\source\repos\just-your-feedback\color")
model_trainer.trainModel(num_objects=2, num_experiments=20, enhance_data=False, batch_size=32, show_network_summary=True)
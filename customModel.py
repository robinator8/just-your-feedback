import PIL

from imageai.Prediction import ImagePrediction
from imageai.Prediction.Custom import ModelTraining

model_trainer = ModelTraining()
prediction = ImagePrediction()

model_trainer.setModelTypeAsInceptionV3()
model_trainer.setDataDirectory(r"C:\Users\Adrian\source\repos\just-your-feedback\color")
model_trainer.trainModel(num_objects=2, num_experiments=10, enhance_data=True, batch_size=32, show_network_summary=True)
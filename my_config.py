class Config:
    def __init__(self):
        self.model = self.Model()
        self.train = self.Train()
        self.data = self.Data()

    class Model:
        def __init__(self):
            self.input_size = 784
            self.hidden_layers = [128, 64]
            self.output_size = 10

    class Train:
        def __init__(self):
            self.batch_size = 256
            self.num_epochs = 10
            self.learning_rate = 0.9
            self.device = None
            self.seed = 42

    class Data:
        def __init__(self):
            self.shuffle = True
            self.augmentation = False
            self.num_workers = 0
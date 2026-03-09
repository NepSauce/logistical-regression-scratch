import csv

class LogisticRegressionScratch:
    def __init__(self, learning_rate, w, b, lambda_):
        self.learning_rate = learning_rate
        self.lambda_ = lambda_
        self.x_train = []
        self.y_train = []
        self.w = w
        self.b = b
        self.column_count = 0
        self.row_count = 0

    def load_csv(self, file_path):
        try:
            with open(file_path, 'r') as file:
                csv_reader = csv.reader(file, delimiter=',')
                header = next(csv_reader)
                self.column_count = len(header)

                for row in csv_reader:
                    self.x_train.append([float(value) for value in row[:-1]])
                    self.y_train.append(float(row[-1]))
                    self.row_count += 1
            
            n_features = self.column_count - 1
            self.w = [0.0] * n_features

            return header
        
        except Exception as e:
            print(f"Error loading CSV: {e}")

            return None
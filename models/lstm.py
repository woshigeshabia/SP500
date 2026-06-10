class LSTMModel(nn.Module):

    def __init__(
        self,
        input_size,
        hidden_size
    ):
        super().__init__()

        self.lstm = nn.LSTM(
            input_size,
            hidden_size,
            batch_first=True
        )

        self.fc = nn.Linear(
            hidden_size,
            1
        )

    def forward(self,x):

        out,_=self.lstm(x)

        return self.fc(
            out[:,-1,:]
        )

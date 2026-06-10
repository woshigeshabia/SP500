class GRUModel(nn.Module):

    def __init__(
        self,
        input_size,
        hidden_size
    ):
        super().__init__()

        self.gru = nn.GRU(
            input_size,
            hidden_size,
            batch_first=True
        )

        self.fc = nn.Linear(
            hidden_size,
            1
        )

    def forward(self,x):

        out,_=self.gru(x)

        return self.fc(
            out[:,-1,:]
        )

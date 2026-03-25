import typer
from bot.orders import place_order
from bot.validators import validate_inputs

app = typer.Typer()

@app.command()
def trade(symbol: str, side: str, order_type: str, quantity: float, price: float = None):
    validate_inputs(symbol, side, order_type, quantity, price)
    response = place_order(symbol, side, order_type, quantity, price)
    typer.echo(response)

if __name__ == "__main__":
    app()

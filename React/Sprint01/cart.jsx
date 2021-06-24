import React from "react";

const Product = ({ product, updateProduct }) => {
    const plus = () => {
        updateProduct({
            ...product,
            count: product.count + 1
        });
    };
    const minus = () => {
        updateProduct({
            ...product,
            count: product.count - 1
        });
    };
    return (
        <div>
            <h3>{product.name}</h3>
            <p>{product.price}</p>
            <button onClick={minus}>-</button>
            <span>{product.count}</span>
            <button onClick={plus}>+</button>
        </div>
    );
};

const CartTotal = ({ total, clearCart }) => {
    return (
        <div>
            <h1>{total}</h1>
            <p>В том числе НДС: {total * 0.2}</p>
            <button onClick={clearCart}>Очистить корзину</button>
        </div>
    );
};

export default class Cart extends React.Component {
    state = {
        cart: [
            {
                id: 1,
                name: "Скафандр",
                count: 1,
                price: 19345
            },
            {
                id: 2,
                name: "Сельдереевый смузи",
                count: 3,
                price: 46
            },
            {
                id: 3,
                name: "Запасной парашют",
                count: 1,
                price: 1870
            }
        ]
    };

    updateProduct = (product) => {
        const currentProduct = this.state.cart.findIndex(
            (p) => p.id === product.id
        );
        if (currentProduct !== -1) {
            const newCart = [...this.state.cart];
            if (product.count) {
                newCart[currentProduct] = product;
                this.setState({ cart: newCart });
            } else {
                const res = window.confirm("Удалить " + product.name + "?");
                if (res) {
                    newCart.splice(currentProduct, 1);
                    this.setState({ cart: newCart });
                }
            }
        }
    };
    clearCart = () => {
        this.setState({ cart: [] });
    };

    render() {
        const total = this.state.cart.reduce((acc, p) => acc + p.price * p.count, 0);

        return (
            <>
                {this.state.cart.map((product) => (
                    <Product
                        product={product}
                        key={product.id}
                        updateProduct={this.updateProduct}
                    />
                ))}
                <CartTotal total={total} clearCart={this.clearCart} />
            </>
        );
    }
}
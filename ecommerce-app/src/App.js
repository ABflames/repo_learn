import React, { useState } from "react";
import "./App.css";


function ProductCard({ product }) {
  return (
    <div className="card">
      <img src={product.image} alt={product.name} />
      <h3>{product.name}</h3>
      <p className="price">₹{product.price}</p>
      <p>{product.description}</p>
    </div>
  );
}


function ProductList({ products }) {
  return (
    <div className="grid">
      {products.map((product) => (
        <ProductCard key={product.id} product={product} />
      ))}
    </div>
  );
}


export default function App() {
  const [products] = useState([
    {
      id: 1,
      name: "Wireless Headphones",
      price: 1999,
      image: "headphones.jpg",
      description: "High-quality sound with noise cancellation",
    },
    {
      id: 2,
      name: "Smart Watch",
      price: 2999,
      image: "smartwatch.jpg",
      description: "Track fitness and notifications",
    },
    {
      id: 3,
      name: "Gaming Mouse",
      price: 999,
      image: "gamingmouse.jpg",
      description: "Ergonomic design with RGB lighting",
    },
    {
      id: 4,
      name: "Laptop Stand",
      price: 799,
      image: "laptopstand.jpg",
      description: "Adjustable and portable",
    },
    {
      id: 5,
      name: "Bluetooth Speaker",
      price: 1499,
      image: "bluetoothspeaker.jpg",
      description: "Powerful bass with long battery life",
    },
  ]);

  return (
    <div className="App">
      <h1>Product Catalog</h1>
      <ProductList products={products} />
    </div>
  );
}


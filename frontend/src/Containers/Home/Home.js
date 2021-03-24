import React from "react";

import { useSelector } from "react-redux";

import styles from "./Home.module.css";

import Button from "../../Components/Button";

const Home = () => {
	const exampleState = useSelector((state) => state.example.exampleState);

	return (
		<div className={styles.container}>
			<h1>Home Component</h1>

			<span>Example State Value : {exampleState}</span>

			<Button title="Sample Button" />
		</div>
	);
};

export default Home;

import React from "react";
import { useSelector } from "react-redux";
import { useHistory } from "react-router-dom";

import Button from "../../Components/Button";

import styles from "./Landing.module.css";

import { ReactComponent as Hero } from "../../Assets/Images/hero.svg";

const Landing = () => {
	const { isLoggedIn } = useSelector((state) => state.auth);

	const history = useHistory();

	const handleProceed = () => {
		if (isLoggedIn) history.push("/dashboard");
		else window.location.href = "http://localhost:8000/oauth2/login";
	};

	return (
		<div className={styles.container}>
			<div className={styles.info}>
				<h1>Formica</h1>
				<h2>In-Discord Forms Solution</h2>
				<p>
					Formica allows you to create forms and collect responses from users without having them ever leave
					their favourite app, Discord! Formica is fully transparent and allows users to see where their data
					is being shared and allows them to delete the data if they wish to.
				</p>
				<Button title="Let's Go!" onClick={handleProceed} />
			</div>
			<div>
				<Hero className={styles.hero} />
			</div>
		</div>
	);
};

export default Landing;

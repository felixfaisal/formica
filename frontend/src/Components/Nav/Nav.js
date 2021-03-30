import React from "react";
import { Link, useHistory } from "react-router-dom";
import { useDispatch, useSelector } from "react-redux";

import Button from "../Button";

import styles from "./Nav.module.css";

import { ReactComponent as DiscordLogo } from "../../Assets/Images/discord.svg";

const Nav = () => {
	const { isLoggedIn } = useSelector((state) => state.auth);
	const dispatch = useDispatch();
	const history = useHistory();

	const handleLogin = async () => {
		dispatch({ type: "LOGIN" });
		history.push("/dashboard");
	};

	return (
		<nav className={styles.nav}>
			<Link to="/" className={styles.brand}>
				<DiscordLogo className={styles.logo} />
				<h2>Formica</h2>
			</Link>

			{isLoggedIn ? (
				<Link to="/dashboard" className={styles.brand}>
					<h2>Guna Shekar</h2>
					<DiscordLogo className={styles.logo} />
				</Link>
			) : (
				<Button title="Login" onClick={handleLogin} />
			)}
		</nav>
	);
};

export default Nav;

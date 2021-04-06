import React, { useState, useEffect } from "react";
import { Link, useLocation } from "react-router-dom";
import { useDispatch, useSelector } from "react-redux";

import Button from "../Button";
import Toast from "../Toast";

import { getUserInformation } from "../../Redux/ActionCreators/user.creator";

import styles from "./Nav.module.css";

import { ReactComponent as DiscordLogo } from "../../Assets/Images/discord.svg";

const useQuery = () => {
	return new URLSearchParams(useLocation().search);
};

const Nav = () => {
	const [loginText, setLoginText] = useState("Loading...");
	const { isLoggedIn } = useSelector((state) => state.auth);
	const { name } = useSelector((state) => state.user);

	const dispatch = useDispatch();
	const query = useQuery();

	useEffect(() => {
		const token = query.get("user");
		if (!token) setLoginText("Login");
		else handleReceivedToken(token);
	}, []);

	const handleReceivedToken = (token) => {
		try {
			dispatch(getUserInformation(token));
		} catch (err) {
			throw err;
		}
	};

	const handleLogin = async () => {
		window.location.href = "http://localhost:8000/oauth2/login";
	};

	return (
		<nav className={styles.nav}>
			<Link to="/" className={styles.brand}>
				<DiscordLogo className={styles.logo} />
				<h2>Formica</h2>
			</Link>

			{isLoggedIn ? (
				<Link to="/dashboard" className={styles.brand}>
					<h2>{name}</h2>
					<DiscordLogo className={styles.logo} />
				</Link>
			) : (
				<Button title={loginText} onClick={handleLogin} />
			)}
		</nav>
	);
};

export default Nav;

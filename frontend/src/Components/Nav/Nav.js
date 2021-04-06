import React, { useState, useEffect } from "react";
import { Link, useLocation, useHistory } from "react-router-dom";
import { useDispatch, useSelector } from "react-redux";

import Button from "../Button";
import Toast from "../Toast";

import { getUserInformation } from "../../Redux/ActionCreators/user.creator";
import { LOGOUT } from "../../Redux/ActionTypes";

import styles from "./Nav.module.css";

import { ReactComponent as DiscordLogo } from "../../Assets/Images/discord.svg";
import { ReactComponent as Logout } from "../../Assets/Images/logout.svg";

const useQuery = () => {
	return new URLSearchParams(useLocation().search);
};

const Nav = () => {
	const [loginText, setLoginText] = useState("Loading...");
	const { isLoggedIn } = useSelector((state) => state.auth);
	const { name, userId, avatar } = useSelector((state) => state.user);

	const dispatch = useDispatch();
	const query = useQuery();
	const history = useHistory();

	useEffect(() => {
		const token = query.get("user");
		if (!token) setLoginText("Login");
		else handleReceivedToken(token);
	}, []);

	const handleReceivedToken = async (token) => {
		try {
			await dispatch(getUserInformation(token));
			Toast("Successfully Logged In!", "success");
			history.push("/dashboard");
		} catch (err) {
			Toast("Invalid Credentials!", "error");
		}
	};

	const handleLogin = async () => {
		window.location.href = "http://localhost:8000/oauth2/login";
	};

	const handleLogout = () => {
		dispatch({ type: LOGOUT });
		Toast("Successfully Logged Out!", "success");
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
					<img src={`https://cdn.discordapp.com/avatars/${userId}/${avatar}`} className={styles.logo} />
					<Logout className={styles.logout} onClick={handleLogout} />
				</Link>
			) : (
				<Button title={loginText} onClick={handleLogin} />
			)}
		</nav>
	);
};

export default Nav;

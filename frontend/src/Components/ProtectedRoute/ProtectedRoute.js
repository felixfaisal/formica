import React from "react";
import { useSelector } from "react-redux";
import { Redirect } from "react-router-dom";

const ProtectedRoute = ({ children }) => {
	const { isLoggedIn } = useSelector((state) => state.auth);
	console.log(isLoggedIn);
	return isLoggedIn ? children : <Redirect to="/" />;
};

export default ProtectedRoute;

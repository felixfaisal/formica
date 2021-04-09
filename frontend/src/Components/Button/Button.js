import React from "react";

import styles from "./Button.module.css";

const Button = ({ title, onClick, className, disabled }) => {
	return (
		<button onClick={onClick} className={`${styles.button} ${disabled && styles.disabled} ${className}`}>
			{title}
		</button>
	);
};

export default Button;

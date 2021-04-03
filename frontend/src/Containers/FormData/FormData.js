import React from "react";
import { useParams } from "react-router";

import styles from "./FormData.module.css";

import formData from "../../Assets/Data/formData";

const FormData = () => {
	const { id } = useParams();

	const displayHeadings = Object.keys(formData[0]).map((key) => <div className={styles.heading}>{key}</div>);

	const displayRow = (row) => Object.keys(row).map((key) => <div className={styles.data}>{row[key]}</div>);

	const displayRows = formData.map((row) => <div className={styles.row}>{displayRow(row)}</div>);

	return (
		<>
			<h3 className={styles.title}>Form {id} :- </h3>
			<div className={styles.container}>
				<div className={styles.row}>{displayHeadings}</div>
				{displayRows}
			</div>
		</>
	);
};

export default FormData;

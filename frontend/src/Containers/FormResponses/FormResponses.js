import React, { useState } from "react";
import CsvDownload from "react-json-to-csv";

import Button from "../../Components/Button";

import styles from "./FormResponses.module.css";

const FormResponses = ({ responses }) => {
	const [checked, setChecked] = useState(false);

	const displayHeadings = responses[0]
		? Object.keys(responses[0]).map((key) => <div className={styles.heading}>{key}</div>)
		: null;

	const displayRow = (row) => Object.keys(row).map((key) => <div className={styles.data}>{row[key]}</div>);

	const displayRows = responses.map((row) => <div className={styles.row}>{displayRow(row)}</div>);

	return responses[0] ? (
		<div className={styles.container}>
			<label className={styles.label}>
				<input
					type="checkbox"
					className={styles.checkbox}
					checked={checked}
					onChange={() => setChecked(!checked)}
				/>
				I understand that the responses may contain personal data of users and sharing it with external sources
				may lead to legal consequences.
			</label>
			{!checked ? (
				<Button title="Download Data" className={styles.button} disabled />
			) : (
				<CsvDownload
					data={responses}
					filename="form_responses.csv"
					style={{
						backgroundColor: "#ff8906",
						border: "none",
						outline: "none",
						color: "#fffffe",
						padding: "1vw",
						paddingLeft: "2vw",
						paddingRight: "2vw",
						cursor: "pointer",
						borderRadius: "5px",
						fontSize: "24px",
						fontWeight: "bold",
						fontFamily: "sans-serif",
						backgroundPosition: "center",
					}}
				>
					Download Data
				</CsvDownload>
			)}

			<div className={styles.row}>{displayHeadings}</div>
			{displayRows}
		</div>
	) : (
		<h3 className={styles.heading}>No Responses Yet!</h3>
	);
};

export default FormResponses;

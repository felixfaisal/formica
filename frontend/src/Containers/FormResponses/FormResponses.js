import React from "react";
import CsvDownload from "react-json-to-csv";

import styles from "./FormResponses.module.css";

const FormResponses = ({ responses }) => {
	const displayHeadings = responses[0]
		? Object.keys(responses[0]).map((key) => <div className={styles.heading}>{key}</div>)
		: null;

	const displayRow = (row) => Object.keys(row).map((key) => <div className={styles.data}>{row[key]}</div>);

	const displayRows = responses.map((row) => <div className={styles.row}>{displayRow(row)}</div>);

	return responses[0] ? (
		<div className={styles.container}>
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
					fontFamily: "Volkorn",
					backgroundPosition: "center",
				}}
			>
				Download Data
			</CsvDownload>
			<div className={styles.row}>{displayHeadings}</div>
			{displayRows}
		</div>
	) : (
		<h3 className={styles.heading}>No Responses Yet!</h3>
	);
};

export default FormResponses;

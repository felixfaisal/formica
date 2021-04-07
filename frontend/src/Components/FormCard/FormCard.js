import React from "react";
import { Link } from "react-router-dom";

import styles from "./FormCard.module.css";

import { ReactComponent as Person } from "../../Assets/Images/person.svg";
import { ReactComponent as Send } from "../../Assets/Images/send.svg";

const FormCard = ({ id, title, responses, shared, accepting = true }) => {
	return (
		<Link className={styles.card_container} to={`forms/${id}/responses`}>
			<h2 className={styles.card_title}>
				{title.slice(0, 25)}
				{title.length > 25 ? "..." : null}
			</h2>
			{/* <div className={styles.stats_container}>
				<span>
					<Person />
					<h3>{responses}</h3>
				</span>
				<span>
					<h3>{shared}</h3>
					<Send />
				</span>
			</div> */}
			<h3 className={styles.status}>
				<span className={accepting ? styles.accepting : styles.not_accepting} />
				{!accepting ? "Not " : null}Accepting Responses
			</h3>
		</Link>
	);
};

export default FormCard;

import React, { useState, useEffect } from "react";
import LineChart from "react-linechart";

import styles from "./FormStatistics.module.css";

import formData from "../../Assets/Data/formData";

const FormStatistics = () => {
	const [data, setData] = useState([]);

	const modifyStatistics = () => {
		const dayWiseObject = {};

		formData.forEach((row) => {
			const date = new Date(row.timestamp).toISOString().split("T")[0];
			if (dayWiseObject[date]) dayWiseObject[date]++;
			else dayWiseObject[date] = 1;
		});

		const dayWiseArray = Object.keys(dayWiseObject).map((key) => ({ x: key, y: dayWiseObject[key] }));
		setData([
			{
				color: "steelblue",
				points: dayWiseArray,
			},
		]);
	};

	useEffect(() => {
		modifyStatistics();
	}, []);

	return <LineChart width={600} height={400} data={data} isDate />;
};

export default FormStatistics;

import { toast } from "react-toastify";

import styles from "./Toast.module.css";

export default (message, type) =>
	toast(message, {
		type,
		className: styles[`notify_${type}`],
		position: "bottom-right",
		autoClose: 3000,
		hideProgressBar: false,
		closeOnClick: true,
		pauseOnHover: true,
		draggable: true,
	});

import axios from 'axios';
import { EXAMPLE_URL } from '../Utils/constants';

export const exampleService = async () => {
  try {
    const {data} = await axios.get(EXAMPLE_URL);
    return data;
  } catch (err) {
    throw err;
  }
}
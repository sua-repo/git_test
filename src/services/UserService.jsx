import axios from "axios";

const getUsers = async () => {
  try {
    const response = await axios.get(
      'https://jsonplaceholder.typicode.com/posts'
    );
    //console.log(response);
    return response.data;
  } catch (error) {
    console.log('Error >>', error);
  }
};

const getUsers2 = async () => {
    try {
      const response = await axios.get(
        'https://jsonplaceholder.typicode.com/posts'
      );
      //console.log(response);
      return response.data;
    } catch (error) {
      console.log('Error >>', error);
    }
  };
export default { getUsers, getUsers2 }  // 같을 경우엔 { getUsers }
import { axiosInstance } from "./axiosInstance";


function getGroups() {
    return axiosInstance.get("/groups/").then(res => res.data);
};

export default getGroups;

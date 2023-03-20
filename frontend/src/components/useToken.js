import { useState } from "react";

export default function useToken() {
  const getToken = () => {
    const accessToken = sessionStorage.getItem('access');
    return accessToken
  };

  const [accessToken, setToken] = useState(getToken());

  const saveToken = accessToken => {
    sessionStorage.setItem('access', accessToken);
    setToken(accessToken);
  }

  return {
    accessToken,
    setToken: saveToken
  }
}

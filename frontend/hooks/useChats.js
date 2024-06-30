import { useEffect, useState } from "react";
import apiClient from "../utils/api-client";

const useChats = (endpoint = "/chat_message/") => {
  const [chats, setChats] = useState([]);
  const [error, setError] = useState("");
  const [isLoading, setLoading] = useState(false);

  const fetchChats = async () => {
    setLoading(true);
    try {
      const response = await apiClient.get(endpoint);
      setChats(response.data);
      setLoading(false);
    } catch (error) {
      setError(error.message);
      setLoading(false);
    }
  };

  useEffect(() => {
    fetchChats();
  }, []);

  return {
    chats,
    error,
    isLoading,
    setLoading,
    refetchChats: fetchChats, // Expose fetchChats as refetchChats for manual re-fetching
  };
};

export default useChats;

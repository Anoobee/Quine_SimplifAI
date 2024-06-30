import { Box, Flex, VStack } from "@chakra-ui/react";
import ChatMessage from "./ChatMessage";
import ChatInput from "./ChatInput";
import { useEffect, useState, useRef } from "react";
import useChats from "../../hooks/useChats";
import apiClient from "../../utils/api-client";

const ChatUI = ({chatMode, isEnglish}) => {
  // const [messages, setMessages] = useState([
  //   {
  //     id: 1,
  //     text: "Summarize the Report",
  //     timestamp: "3 minutes ago",
  //     sender: "Anup Aryal",
  //     isUser: true,
  //   },
  //   {
  //     id: 2,
  //     text: "By following this structured approach, you can create a clear and concise summary of any health report...",
  //     timestamp: "3 minutes ago",
  //     sender: "SimplifAI",
  //     isUser: false,
  //   },
  // ]);

  const { chats, error, isLoading, setLoading, refetchChats } = useChats();
  console.log(isLoading, "loading");
  const [newMessage, setNewMessage] = useState("");
  const [localMessages, setLocalMessages] = useState([]);
  const bottomRef = useRef(null);

  useEffect(() => {
    bottomRef.current.scrollIntoView({ behavior: "smooth" });
  }, [chats]);

  useEffect(() => {
    bottomRef.current.scrollIntoView({ behavior: "smooth" });
  }, [isLoading]);


  const handleSend = () => {
    console.log(chats);
    console.log(isEnglish, "english");
    console.log(chatMode, "chatmode");
    setLoading(true);
    if (newMessage.trim()) {
      const messageToSend = {
        id: Date.now(), // Using timestamp as a temporary ID
        text: newMessage,
        timestamp: "Just now",
        sender: "Anup Aryal",
        isUser: true,
        isDoctor: chatMode === "Doctor" ? true : false,
        isEnglish: isEnglish,
      };

      // Optionally update local state immediately for better UX
      console.log(messageToSend, "local");
      setLocalMessages([messageToSend]);

      //when user cicks the send button -> state ma message to send
      //when response gets fetched -> remove
      // Post request to send the message to the backend
      setNewMessage("");
      apiClient
        .post("/chat_message/", messageToSend)
        .then((response) => {
          console.log("response is fetched");
          setLoading(false);
          setLocalMessages([""]);
          refetchChats();

          // Clear input after successful send
        })
        .catch((error) => {
          console.error("Failed to send message:", error);
          // Optionally handle failed send, e.g., remove from localMessages
        });
    }
  };
  console.log("local", localMessages, "chat", chats);
  return (
    <Flex direction="column" height="100vh">
      <VStack flex="1" overflowY="auto" p={4} spacing={4}>
        {[...chats].map((msg) => (
          <ChatMessage
            key={msg.id}
            message={msg.text}
            timestamp={msg.timestamp}
            sender={msg.sender}
            isUser={msg.isUser}
          />
        ))}
        <div ref={bottomRef} />
      </VStack>
      <Box position="sticky" bottom="60px">
        <ChatInput
          value={newMessage}
          onChange={(e) => setNewMessage(e.target.value)}
          handleSend={handleSend}
          isLoading={isLoading}
        />
        {console.log(isLoading, "loading")}
      </Box>
    </Flex>
  );
};

export default ChatUI;

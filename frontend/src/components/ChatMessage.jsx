import React from "react";
import { Text, Avatar, HStack, VStack } from "@chakra-ui/react";
import Markdown from "react-markdown";
import remarkGfm from "remark-gfm";

const ChatMessage = ({ message, timestamp, sender, isUser }) => {
  return (
    <HStack
      alignSelf={isUser ? "flex-end" : "flex-start"}
      bg={isUser ? "teal.100" : "gray.100"}
      borderRadius="lg"
      p={3}
      spacing={3}
      m={2}
    >
      {!isUser && <Avatar name={sender} alignSelf="flex-start" />}
      <VStack align={isUser ? "flex-end" : "flex-start"}>
          <Markdown remarkPlugins={[remarkGfm]}>{message}</Markdown>
        <Text fontSize="xs" color="gray.500">
          {timestamp}
        </Text>
      </VStack>
      {isUser && <Avatar name={sender} />}
    </HStack>
  );
};

export default ChatMessage;

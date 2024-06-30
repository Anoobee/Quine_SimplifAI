import { Box, Text, Flex } from "@chakra-ui/react";

const ChatList = ({ title, items }) => {
  return (
    <Box m={4}>
      <Text fontSize="xl" fontWeight="bold" mb={4}>
        {title}
      </Text>
      {items.map((item, index) => (
        <Flex
          key={index}
          bg="gray.100"
          p={4}
          borderRadius="md"
          mb={2}
          direction="column"
        >
          <Text fontWeight="bold">{item.title}</Text>
          <Text fontSize="sm">
            {item.time} - {item.user}
          </Text>
        </Flex>
      ))}
    </Box>
  );
};

export default ChatList;

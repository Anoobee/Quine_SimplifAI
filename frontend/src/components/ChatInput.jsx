import { Box, Flex, Input, IconButton, Spinner } from "@chakra-ui/react";
import { FaPaperPlane } from "react-icons/fa";

const ChatInput = ({ value, onChange, handleSend, isLoading }) => {
  return (
    <Box>
      <Flex p={4} align="center" bg="white" boxShadow="md">
        <Input
          placeholder="Type your message..."
          value={value}
          onChange={onChange}
          mr={2}
        />
        {console.log(isLoading, "loading")}
        {isLoading?<Spinner
        thickness='4px'
        speed='0.65s'
        emptyColor='gray.200'
        color='blue.500'
        size='lg'
      />:<IconButton
      icon={<FaPaperPlane />}
      colorScheme="teal"
      onClick={handleSend}
      aria-label="Send message"
    />}
      </Flex>
    </Box>
  );
};

export default ChatInput;

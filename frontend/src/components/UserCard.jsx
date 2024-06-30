import React from "react";
import { Box, Avatar, Text, Input, Flex, IconButton } from "@chakra-ui/react";
import { FaBell } from "react-icons/fa";

const UserCard = () => {
  return (
    <Box bg="teal.100" p={4} borderRadius="md" m={4}>
      <Flex alignItems="center">
        <Avatar size="lg" name="Aashish Karki" src="../assets/userProfile.jpeg" />
        <Box ml={4}>
          <Text>Hello, Welcome 🎉</Text>
          <Text fontWeight="bold" fontSize="lg">
            Aashish Karki
          </Text>
          <Input mt={2} placeholder="Search chat" size="sm" />
        </Box>
        <IconButton
          icon={<FaBell />}
          variant="ghost"
          aria-label="Notifications"
          ml="auto"
        />
      </Flex>
    </Box>
  );
};

export default UserCard;

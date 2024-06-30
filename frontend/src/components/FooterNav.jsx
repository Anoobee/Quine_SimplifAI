import { Box, IconButton, Flex } from "@chakra-ui/react";
import { FaHome, FaCommentDots } from "react-icons/fa";
import { Link } from "react-router-dom";
import { Spinner } from '@chakra-ui/react';

const FooterNav = ({ isLoading }) => {
  return (
    <Box bg="gray.100" p={4} position="relative" bottom="0" width="100%">
      <Flex justifyContent="space-around">
        <Link to="/home">
          <IconButton icon={<FaHome />} variant="ghost" aria-label="Home" />
        </Link>

        <Link to="/chat">
          {isLoading ? (
            <Spinner size="xl" color="blue.500" thickness="4px" speed="0.65s" emptyColor="gray.200" />
          ) : (
            <IconButton
              icon={<FaCommentDots />}
              variant="ghost"
              aria-label="Messages"
            />
          )}
        </Link>
      </Flex>
    </Box>
  );
};

export default FooterNav;

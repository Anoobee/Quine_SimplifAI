import { Box, Flex, IconButton, Heading, Spacer } from '@chakra-ui/react';
import { FaUserCircle, FaBars } from 'react-icons/fa';

const Header = () => {
  return (
    <Box bg="gray.100" p={4} top='0' width="100%">
      <Flex alignItems="center">
        <IconButton
          icon={<FaBars />}
          variant="ghost"
          aria-label="Menu"
        />
        <Heading as="h1" size="lg" ml={2}>
          SimplifAI
        </Heading>
        <Spacer />
        <IconButton
          icon={<FaUserCircle />}
          variant="ghost"
          aria-label="User Profile"
        />
      </Flex>
    </Box>
  );
};

export default Header;

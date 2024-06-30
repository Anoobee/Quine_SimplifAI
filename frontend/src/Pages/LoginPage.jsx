import React from "react";
import {
  Box,
  Button,
  Center,
  Flex,
  FormControl,
  FormLabel,
  Heading,
  Input,
  VStack,
  Text,
} from "@chakra-ui/react";
import { Link } from "react-router-dom";

const LoginPage = () => {
  return (
    <Flex
      direction="column"
      height="100vh"
      justifyContent="center"
      alignItems="center"
      width="100%"
    >
      <Box
        bg="white"
        p={8}
        borderRadius="md"
        boxShadow="lg"
        width="100%"
        maxWidth="400px"
      >
        <Center mb={6}>
          <Heading as="h1" size="xl" color="teal.500">
            SimplifAI
          </Heading>
        </Center>
        <VStack spacing={4} align="stretch">
          <FormControl>
            <FormLabel>Email</FormLabel>
            <Input type="email" placeholder="Enter your email" />
          </FormControl>
          <FormControl>
            <FormLabel>Password</FormLabel>
            <Input type="password" placeholder="Enter your password" />
          </FormControl>
          <Button colorScheme="teal" size="lg" width="100%">
            Login
          </Button>
          <Link to="/home">
            <Button colorScheme="gray" variant="outline" size="lg" width="100%">
              Login as Guest
            </Button>
          </Link>
        </VStack>
        <Text mt={4} textAlign="center">
          Don't have an account?{" "}
          <Button variant="link" colorScheme="teal">
            Sign Up
          </Button>
        </Text>
      </Box>
    </Flex>
  );
};

export default LoginPage;

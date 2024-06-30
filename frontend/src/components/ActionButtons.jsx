import { useRef, useState, useEffect } from "react";
import { Box, Button, Flex } from "@chakra-ui/react";
import axios from "axios";

const ActionButtons = ({ setIsLoading, chatMode, isEnglish }) => {
  const [image, setImage] = useState(null);
  const fileInputRef = useRef(null);
  const captureInputRef = useRef(null);

  useEffect(() => {
    if (image) {
      handleAPI();
    }
  }, [image]);

  const handleImage = (e) => {
    const file = e.target.files[0];
    console.log(file);
    if (file) {
      setImage(file);
    }
  };
  const handleUploadClick = () => {
    setIsLoading(true);
    fileInputRef.current.click();
  };
  const handleCaptureClick = () => {
    setIsLoading(true);
    captureInputRef.current.click();
  };

  const handleAPI = () => {
    const formData = new FormData();
    formData.append("plot", image);
    formData.append("isDoctor", chatMode == "Doctor" ? "True" : "False");
    formData.append("isEnglish", isEnglish == true ? "True" : "False");
    console.log(formData);
    axios
      .post("http://127.0.0.1:8000/upload_report/", formData)
      // .post("http://192.168.1.10:8000/upload_report/", formData)
      .then((res) => {
        console.log(res);
        setTimeout(() => {
          setIsLoading(false);
        }, 15000);
      })
      .catch((err) => {
        console.log(err);
      });
  };

  return (
    <Box p={4} pb={4}>
      <Flex justifyContent="space-around">
        <input
          type="file"
          ref={fileInputRef}
          style={{ display: "none" }}
          onChange={handleImage}
        />
        <input
          type="file"
          accept="image/*"
          style={{ display: "none" }}
          ref={captureInputRef}
          capture="environment"
          onChange={handleImage}
        />
        <Button colorScheme="teal" variant="solid" onClick={handleUploadClick}>
          Upload File
        </Button>
        <Button colorScheme="teal" variant="solid" onClick={handleCaptureClick}>
          Capture
        </Button>
      </Flex>
    </Box>
  );
};

export default ActionButtons;

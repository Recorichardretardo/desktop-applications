import React, { useEffect, useState } from 'react';
import { useDispatch, useSelector } from 'react-redux';
import { Container, Card, Button, Modal, Spinner   } from 'react-bootstrap';
// import {Modal, ModalHeader, ModalBody, ModalFooter} from 'reactstrap';
import styled from 'styled-components';
import { getPosts } from '../../redux-store/actions/TestCard';
import Table from '../../components/TestTable';
import CustomSpinner from '../../components/CustomSpinner';

const CustomLabel = styled.label`
  color: #FFFFFF;
  font-size: 1rem;
  margin-top: 15px;
  font-weight: 500;
`;


const Home = (props) => {
    const dispatch = useDispatch();
    const testCardDataa = useSelector(state => state.testCard) || {};

    const {
        buttonLabel,
        className
      } = props;

    const [show, setShow] = useState(false);

    const handleClose = () => setShow(false);
    const handleShow = () =>{
        setShow(true)
        setInterval(() => {
            setShow(false)
        }, 5000)
       
    };

    const [modal, setModal] = useState(false);

  const toggle = () => setModal(!modal);


    useEffect(() => {
        window.scrollTo(0, 0);
        dispatch(getPosts());
    }, [dispatch]);

    console.log("testCardDataa", testCardDataa);
return (<>
    <Container>
        <Card style={{ height: '3.5rem', textAlign: 'center', backgroundColor: '#000000', marginTop: '15px'}} >
            <CustomLabel> Home</CustomLabel>
        </Card>
        <Table />

        <Button variant="primary" onClick={handleShow}>
        Launch demo modal
      </Button>

      <Modal dialogClassName='m-dialog' size='xl' keyboard={false} centered={true} contentClassName='c-name' show={show} onHide={handleClose} backdrop="static">
        <Modal.Header className='m-header' closeButton={true}>
          <Modal.Title>Modal heading</Modal.Title>
        </Modal.Header>
        <Modal.Body>
            <CustomSpinner />
        {/* <Spinner animation="border" role="status">
  <span className="visually-hidden">Loading...</span>
</Spinner> */}
            Woohoo, you're reading this text in a modal!
            
        </Modal.Body>
        <Modal.Footer>
          <Button variant="secondary" onClick={handleClose}>
            Close
          </Button>
          <Button variant="primary" onClick={handleClose}>
            Save Changes
          </Button>
        </Modal.Footer>
      </Modal>


      {/* <div>
      <Button color="danger" onClick={toggle}>{buttonLabel}</Button>
      <Modal isOpen={modal} toggle={toggle} className="custom-modal-style">
        <ModalHeader toggle={toggle}>Modal title</ModalHeader>
        <ModalBody>
          ...
        </ModalBody>
        <ModalFooter>
          <Button color="primary" onClick={toggle}>Do Something</Button>{' '}
          <Button color="secondary" onClick={toggle}>Cancel</Button>
        </ModalFooter>
      </Modal>
    </div> */}
      
    </Container>
</>);
};

export default Home;
import logo from './images/newlogo.png';
import './App.css';
import Dropzone from "react-dropzone";





function App() {


    const onFileChangeHandler = (e) => {


        e.preventDefault()
        const formData = new FormData();

        formData.append('file', e.target.files[0]);

        const options = {
            method: 'POST',
            body: e.target.files[0],
             headers: {
              'Content-Type': 'application/x-image',
             }
        };

        fetch('https://j3qh4wgctk.execute-api.us-west-2.amazonaws.com/v2/predictcovid19', options)
            .then(response => response.json())
            .then(data => alert(data.body))
            .catch(err => console.log(err.response));;



    };




    return (

        <div className="App">

            <div className="App-Header" a>
                <img className="App-Logo" src={logo} alt="logo" />
            </div>
            <div className="App-Body" >


                <Dropzone >
                    {({ getRootProps, getInputProps }) => (
                        <div {...getRootProps({ className: "dropzone" })} align="center">
                            <label htmlFor="file-upload" className="custom-file-upload" >
                                <i className="fa fa-cloud-upload"  ></i>
                            </label>
                            <input {...getInputProps()} accept="image/*" onChange={onFileChangeHandler} />
                            <p>Click above icon to upload a Chest X-ray image. </p>
                        </div>
                    )}
                </Dropzone>


            </div>
        </div>


    );
}

export default App;

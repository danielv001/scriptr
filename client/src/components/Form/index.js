import React, {useState} from 'react'


const Form = ({url, setUrl}) => {
    const [input, setInput] = useState("");
    const handleSubmit = (e) => {
        e.preventDefault()
        setUrl(input)

    }
    return (
        <div>
             <div className="row">
                <form className="col s12" onSubmit={handleSubmit}>
                    <div className="row" style={{display: "flex"}}>
                        <div className="input-field col s10">
                            <textarea onChange={(e) => setInput(e.target.value)}id="textarea1" className="materialize-textarea"></textarea>
                            <label htmlFor="textarea1">Enter URL</label>
                        </div>
                        <div  className="col s2"style={{display: "flex", flexDirection: "column",alignItems: "center", justifyContent: "center"}}>
                        <button className="btn waves-effect waves-light" type="submit" name="action">Submit
                            <i className="material-icons right">send</i>
                        </button>
                        </div>
                    </div>
                </form>
            </div>
        </div>
    )
}

export default Form
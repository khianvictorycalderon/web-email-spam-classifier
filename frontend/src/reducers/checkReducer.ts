export interface CheckResponseProps {
    message: string;
}

interface FetchStateProps {
    data: CheckResponseProps;
    loading: boolean;
    error: string | null;
}

type ActionTypes = 
    | { type: "FETCH_START" }
    | { type: "FETCH_SUCCESS", payload: CheckResponseProps }
    | { type: "FETCH_ERROR", payload: string }

export default async function reducer (
    state: FetchStateProps,
    action: ActionTypes
) {
    
    switch (action.type) {
        case "FETCH_START":
            return {
                ...state,
                loading: true,
                error: null
            }
        case "FETCH_SUCCESS":
            return {
                ...state,
                loading: false,
                data: action.payload
            }
        case "FETCH_ERROR":
            return {
                ...state,
                loading: false,
                error: action.payload
            }
        default:
            return state;
    }

}
interface SubmitButtonInputProps {
    children: string;
}

export default function SubmitButtonInput({
    children
}: SubmitButtonInputProps) {
    return (
        <input 
            className="
                cursor-pointer
                rounded-md
                px-6 py-2 bg-emerald-600 hover:bg-emerald-500 text-white
                transition duration-300
            "
            type="submit" 
            value={children}
          />
    )
}
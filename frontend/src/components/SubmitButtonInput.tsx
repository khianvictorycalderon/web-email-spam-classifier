interface SubmitButtonInputProps {
    children: string;
    disabled?: boolean;
}

export default function SubmitButtonInput({
    children, disabled
}: SubmitButtonInputProps) {
    return (
        <input
            disabled={disabled}
            className="
                cursor-pointer
                rounded-md
                px-6 py-2 bg-emerald-600 hover:bg-emerald-500 text-white
                transition duration-300
                disabled:bg-neutral-400
                disabled:text-neutral-700
                disabled:cursor-not-allowed
            "
            type="submit" 
            value={children}
          />
    )
}
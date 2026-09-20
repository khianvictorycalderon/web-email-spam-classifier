interface ButtonProps {
    children: string;
    className?: string;
    disabled?: boolean;
    onClick: () => void;
}

export default function Button({
    children, className, disabled, onClick
}: ButtonProps) {
    return (
        <button
            className={`
                cursor-pointer
                px-12 py-2 rounded-md
                trasition duration-300
                disabled:bg-neutral-400
                disabled:text-neutral-700
                disabled:cursor-not-allowed
                ${className}
            `}
            onClick={onClick}
            disabled={disabled}
        >{children}</button>
    )
}
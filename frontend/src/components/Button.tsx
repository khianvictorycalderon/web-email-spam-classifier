interface ButtonProps {
    children: string;
    className?: string;
    disabled?: boolean;
}

export default function Button({
    children, className, disabled
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
            disabled={disabled}
        >{children}</button>
    )
}
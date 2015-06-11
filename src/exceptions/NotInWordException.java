package exceptions;

public class NotInWordException extends Exception {
	public NotInWordException() {
		super();
	}
	
	public NotInWordException(String message) {
		super(message);
	}
}

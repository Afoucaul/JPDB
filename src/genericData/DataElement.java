package genericData;

import java.util.*;

public class DataElement {
	private List<String> meanings;
	
	public DataElement() {}
	
	public DataElement(List<String> meanings) {
		this.meanings = new ArrayList();
		for(String meaning : meanings) {
			this.addMeaning(meaning);
		}
	}
	
	public void addMeaning(String meaning) {
		this.meanings.add(meaning);
	}

	public boolean means(String meaning) {
		return this.meanings.contains(meaning);
	}
	
}

package words;
import java.util.*;
import exceptions.NotInListException;
import kanjis.*;

public class WordsManager {
	private List<Word> words;
	
	public WordsManager() {
		this.words = new ArrayList();
	}
	
	public void loadWords() {
		
	}
	
	public void addToTable(Word word) {
		
	}
	
	public void removeFromTable(Word word) {
		
	}
	
	public void updateWordInTable(Word word) {
		
	}
	
	public Word searchByKanjis(List<Kanji> kanjis) throws NotInListException {
		for(Word word : words) {
			boolean flag = true;
			for(Kanji kanji : kanjis) {
				flag &= word.isRelatedTo(kanji);
			}
			if(flag)
				return word;
		}
		throw new NotInListException("No word was found");
	}

	public Word searchByWriting(String writing) throws NotInListException {
		for(Word word : words) {
			if(word.isWritten(writing)) {
				return word;
			}
		}
		throw new NotInListException("No word was found");
	}
	
}
package org.velezreyes.quiz.question6;

public class VendingMachineImpl implements VendingMachine{

  private double cents;
  private Drink drink;
  private final String[] drinksOptions = {"ScottCola", "KarenTea"};


  public VendingMachineImpl() {
    this.cents = 0;
    this.drink = new DrinkImpl();
  }

  public static VendingMachine getInstance() {
    // Fix me!
    return new VendingMachineImpl();
  }

  @Override
  public void insertQuarter() {
    this.cents += 25;
  }

  @Override
  public Drink pressButton(String name) throws NotEnoughMoneyException, UnknownDrinkException {
    if(this.cents <= 0 || (name.equals("KarenTea") && this.cents <= 75)) {
      throw new NotEnoughMoneyException();
    }

    if(!name.equals("ScottCola") && !name.equals("KarenTea")) {
      throw new UnknownDrinkException();
    }

    this.drink.setName(name);
    return this.drink;
  }

}
